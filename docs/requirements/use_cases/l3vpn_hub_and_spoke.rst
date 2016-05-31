.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Bin Hu

Hub and Spoke Case
------------------

Description
~~~~~~~~~~~

There are 2 hosts (compute nodes). SDN Controller A and vRouter A are provided by
Vendor A, and run on host A. SDN Controller B and vRouter B are provided by
Vendor B, and run on host B.

There is 1 tenant. Tenant 1 creates L3VPN Blue with 2 subnets: 10.1.1.0/24 and 10.3.7.0/24.

The network topology is shown in :numref:`l3vpn-hub-spoke-figure`:

.. figure:: images/l3vpn-hub-spoke.png
   :name:  l3vpn-hub-spoke-figure
   :width: 100%

In L3VPN Blue, vFW(H) is acting the role of ``hub`` (a virtual firewall).
The other 3 VNFsVMs are ``spoke``. vFW(H) and VNF1(S) are spawned on host A,
and VNF2(S) and VNF3(S) are spawned on host B. vFW(H) (10.1.1.5) and VNF2(S)
(10.1.1.6) are attached to subnet 10.1.1.0/24. VNF1(S) (10.3.7.9) and VNF3(S)
(10.3.7.10) are attached to subnet 10.3.7.0/24.

Derrived Requirements
~~~~~~~~~~~~~~~~~~~~~

Northbound API / Workflow
+++++++++++++++++++++++++

Exemplary vFW(H) Hub VRF is as follows:

* RD1 10.1.1.5  IP_OVR1 Label1
* RD1 0/0 IP_OVR1 Label1
* Label 1 Local IF (10.1.1.5)
* RD3 10.3.7.9  IP_OVR1 Label2
* RD2 10.1.1.6  IP_OVR2 Label3
* RD4 10.3.7.10 IP_OVR2 Label3

Exemplary VNF1(S) Spoke VRF is as follows:

* RD1 0/0 IP_OVR1 Label1
* RD3 10.3.7.9  IP_OVR1 Label2

Exemplary workflow is described as follows:

1. Create Network

2. Create VRF Policy Resource

  2.1. Hub and Spoke

3. Create Subnet

4. Create Port

  4.1. Subnet

  4.2. VRF Policy Resource, [H | S]

Data model objects
++++++++++++++++++
   - TBD

Orchestration
+++++++++++++
   - TBD

Dependencies on compute services
++++++++++++++++++++++++++++++++
   - TBD

Current implementation
++++++++++++++++++++++

There are multiple different technologies and corresponding projects which allow
for creating a network topology in which traffic is directed through specific
network elements. Among the projects considered here, is [BGPVPN]_ and
[NETWORKING-SFC]_. We investigate the suitability of each project in the
following.


BGPVPN
''''''

Support for creating and managing L3VPNs is in general available in OpenStack
Neutron by means of the BGPVPN project [BGPVPN]_. However, the [BGPVPN]_ API
does not allow to exactly create the hub-and-spoke topology outlined above in a
clean and straightforward manner.

The [BGPVPN]_ API currently supports the concepts of network- and
router-associations. An association in principle maps to a VRF that
interconnects either subnets of a Neutron network (network association) or the
networks connected by a router (router association). It does not yet allow for
creating VRFs per VM port (port associations). This functionality is needed,
however, to create separate VRFs per VM.

Given the network- and router-association mechanisms, the following workflow
establishes a network topology which aims to resemble the desired target
topology. In order to compansate for the missing port association, the basic
idea is to model separate VRFs per VM by creating a dedicated Neutron network
with two subnets for each VRF in the hub-and-spoke topology.

1. Create Neutron network "hub"
  :code:`neutron net-create hub`

2. Create a separate Neutron network for every "spoke"
  :code:`neutron net-create spoke-i`

3. For every network (hub and spokes), create two subnets
  :code:`neutron subnet-create <hub/spoke-i network UUID> 10.1.1.0/24`
  :code:`neutron subnet-create <hub/spoke-i network UUID> 10.3.7.0/24`

4. Create a BGPVPN object (VRF) for the hub network with the corresponding import
   and export targets
  :code:`neutron bgpvpn-create --name hub-vrf --import-targets <RT-hub RT-spoke> --export-targets <RT-hub>`

5. Create a BGPVPN object (VRF) for every spoke network with the corresponding import
   and export targets
  :code:`neutron bgpvpn-create --name spoke-i-vrf --import-targets <RT-hub> --export-targets <RT-spoke>`

6. Associate the hub network with the hub VRF
  :code:`bgpvpn-net-assoc-create hub --network <hub network-UUID>`

7. Associate each spoke network with the corresponding spoke VRF
  :code:`bgpvpn-net-assoc-create spoke-i --network <spoke-i network-UUID>`

After step 7, VMs can be booted on the corresponding networks.

The resulting network topology resembles the target topology as shown in
:numref:`l3vpn-hub-spoke-figure`. However, the workflow for creating this
topology by means of the mechanisms provided by today's implementation deviates
significantly from the desired workflow described above. The gap analysis in the
next section investigates the describes the technical reasons for this.

.. However, the [BGPVPN]_ API does
.. not yet support Spoke and Hub use case in terms of setting up specific VRFs of vFW(H)
.. and other VNFs(S) to create the service chain from vFW(H) to VNFs(S),
.. including those specific I-RT and E-RT at different VRFs.


Network SFC
'''''''''''

Support of Service Function Chaining is in general available in OpenStack Neutron through
the Neutron API for Service Insertion and Chaining project [NETWORKING-SFC]_.
However, the [NETWORKING-SFC]_ API is focused on creating service chaining through
NSH at L2, although it intends to be agnostic of backend implementation. It is unclear whether
or not the service chain from vFW(H) to VNFs(S) can be created in the way of L3VPN-based
VRF policy approach using [NETWORKING-SFC]_ API.

Hence, it is currently not possible to configure the networking use case as described above.


Gaps in Current Solution
++++++++++++++++++++++++

Given the use case description and the currently available implementation in
OpenStack provided by [BGPVPN]_ project and [NETWORKING-SFC]_ project,
we identify the following gaps:

* [L3VPN-HS-GAP1] The [BGPVPN]_ project lacks port-associations

  The workflow described above intents to mimic port associations by means of
  separate Neutron networks. Hence, the resulting workflow is overly complicated
  and not intuitive by requiring to create additional Neutron entities
  (networks) which are not present in the target topology.

  Within the [BGPVPN]_ project, design work on port-association has started. The
  timeline for this feature is however not defined yet. As a result, creating a
  clean hub-and-spoke topology is current not yet supported by the [BGPVPN]_ API.

* [L3VPN-HS-GAP2] Creating a clean hub-and-spoke topology is current not yet supported by the [NETWORKING-SFC]_ API.

