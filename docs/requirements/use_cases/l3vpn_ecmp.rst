.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Bin Hu

ECMP Load Splitting Case (Anycast)
----------------------------------

Description
~~~~~~~~~~~

There are 2 hosts (compute nodes). SDN Controller A and vRouter A are provided by
Vendor A, and run on host A. SDN Controller B and vRouter B are provided by
Vendor B, and run on host B.

There is 1 tenant. Tenant 1 creates L3VPN Blue with subnet 10.1.1.0/24.

The network topology is shown in :numref:`l3vpn-ecmp-figure`:

.. figure:: images/l3vpn-ecmp.png
   :name:  l3vpn-ecmp-figure
   :width: 100%

In L3VPN Blue, VNF1.1 and VNF1.2 are spawned on host A, attached to subnet 10.1.1.0/24
and assigned the same IP address 10.1.1.5. VNF1.3 is spawned on host B, attached to
subnet 10.1.1.0/24 and assigned the same IP addresses 10.1.1.5. VNF 2 and VNF 3 are spawned
on host A and B respectively, attached to subnet 10.1.1.0/24, and assigned different IP
addresses 10.1.1.6 and 10.1.1.3 respectively.

Here, the Network VRF Policy Resource is ``ECMP/AnyCast``. Traffic to **Anycast 10.1.1.5**
can be load split from either WAN GW or another VM like G5.


Derrived Requirements
~~~~~~~~~~~~~~~~~~~~~

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



Current implementation
~~~~~~~~~~~~~~~~~~~~~~

Support for creating and managing L3VPNs is in general available in OpenStack
Neutron by means of the BGPVPN project [BGPVPN]_. However, the BGPVPN project
does not yet support ECMP. Hence, it is currently not possible to configure the
networking use case as described above.

Nevertheless, ECMP load balancing is on the roadmap of the BGPVPN project. The
following workflow shows how to realize this particular use case under the
assumption that support for static routes is available in the BGPVPN API.


1. Create Neutron network for tenant "Blue"

  ``neutron net-create --tenant-id Blue net1``


2. Create subnet for the network of tenant "Blue"

  ``neutron subnet-create --tenant-id Blue --name subnet1 net1 5.1.1.0/24``


3. Create Neutron ports in the network of tenant "Blue"

  ``neutron port-create --tenant-id Blue --name G1 --fixed-ip subnet_id=subnet1,ip_address=5.1.1.1 net1``

  ``neutron port-create --tenant-id Blue --name G2 --fixed-ip subnet_id=subnet1,ip_address=5.1.1.2 net1``

  ``neutron port-create --tenant-id Blue --name G3 --fixed-ip subnet_id=subnet1,ip_address=5.1.1.3 net1``

  ``neutron port-create --tenant-id Blue --name G4 --fixed-ip subnet_id=subnet1,ip_address=5.1.1.4 net1``

  ``neutron port-create --tenant-id Blue --name G5 --fixed-ip subnet_id=subnet1,ip_address=5.1.1.5 net1``

  ``neutron port-create --tenant-id Blue --name G6 --fixed-ip subnet_id=subnet1,ip_address=5.1.1.6 net1``


4. Create a L3VPN for tenant "Blue"

  ``neutron bgpvpn-create --tenant-id Blue --route-target AS:100 vpn1``


5. Associate the BGPVPN with the network of tenant "Blue"

  ``neutron bgpvpn-network-associate --tenant-id Blue --network-id net1 vpn1``


6. Create static routes which point to the same target

  ``neutron bgpvpn-static-route-add --tenant-id Blue --cidr 10.1.1.5/32 --nexthop-ip 5.1.1.1 vpn1``

  ``neutron bgpvpn-static-route-add --tenant-id Blue --cidr 10.1.1.5/32 --nexthop-ip 5.1.1.2  vpn1``

  ``neutron bgpvpn-static-route-add --tenant-id Blue --cidr 10.1.1.5/32 --nexthop-ip 5.1.1.3  vpn1``



Gaps in the current solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given the use case description and the currently available implementation in
OpenStack provided by BGPVPN project, we identify the following gaps:

* [L3VPN-ECMP-GAP1] ECMP is current not yet supported by the BGPVPN API. The
  Development of this feature is on the roadmap of the project, however.
  TODO: add timeline and planned API

* [L3VPN-ECMP-GAP2] It is not possible to assign the same IP to multiple Neutron
  ports within the same Neutron subnet. This is due to the fundamental
  requirement of avoiding IP collisions within the L2 domain which is a Neutron
  network. A potential workaround is to create two subnets with the same IP ranges
  and associate both with the same BGP VPN.



Conclusion
~~~~~~~~~~

TBD
