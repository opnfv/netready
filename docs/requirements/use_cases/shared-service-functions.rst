.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Georg Kunz


Shared Service Functions
------------------------

Description
^^^^^^^^^^^

This use case aims at binding multiple networks or network services to a single
vNIC (port) of a given VM. There are several specific application scenarios for
this use case:

* Shared Service Functions: A service function connects to multiple (tenant)
  networks by means of a single vNIC.

  Typically, a vNIC is bound to a single (tenant) network. Hence, in order to
  directly connect a service function to multiple (tenant) networks at the same
  time, multiple vNICs are needed - each vNIC binding the service function to a
  separate network. For service functions requiring connectivity to a large
  number of networks, this approach does not scale as the number of vNICs per VM
  is limited and additional vNICs occupy additional resources on the hypervisor.

  A more scalable approach is to bind multiple networks to a single vNIC
  and let the service function, which is now shared among multiple networks,
  handle the separation of traffic itself.


* Multiple network services: A service function connects to multiple different
  network types such as a L2 network, a L3(-VPN) network, a SFC domain or
  services such as DHCP, IPv6 NDP, firewall/security, etc.


In order to achieve a flexible binding of multiple services to vNICs, a logical
separation between a vNIC (instance port) - that is, the entity that is used by
the compute service as hand-off point between the network and the VM - and a
service interface - that is, the interface a service binds to - is needed.

Furthermore, binding network services to service interfaces instead of to the
vNIC directly enables a more dynamic management of the network connectivity of
network functions as there is no need to add or remove vNICs.


Requirements
^^^^^^^^^^^^

Northbound API
""""""""""""""

The API has to cover the following functionality:

* management of instance ports

* management of service ports

* binding of services to service ports


Data models
"""""""""""

TBD


Orchestration
"""""""""""""

None.


Dependencies on other resources
"""""""""""""""""""""""""""""""

The compute service needs to be enabled to consume instance ports instead of
classic Neutron ports.


Implementation Proposal
^^^^^^^^^^^^^^^^^^^^^^^

TBD
