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


