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


Derrived Requirements
~~~~~~~~~~~~~~~~~~~~~
   - TBD

Northbound API / Workflow
+++++++++++++++++++++++++
   - TBD

Data model objects
++++++++++++++++++
   - TBD

Orchestration
+++++++++++++
   - TBD

Dependencies on compute services
++++++++++++++++++++++++++++++++
   - TBD

Potential implementation
++++++++++++++++++++++++
   - TBD


