.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Georg Kunz


Port Abstraction
----------------

Description
^^^^^^^^^^^

This use case aims at binding multiple networks or network services to a single
vNIC (port) of a given VM. There are several specific application scenarios for
this use case:

* Shared Service Functions: A service function connects to multiple networks of
  a tenant by means of a single vNIC.

  Typically, a vNIC is bound to a single network. Hence, in order to directly
  connect a service function to multiple networks at the same time, multiple vNICs
  are needed - each vNIC binding the service function to a separate network. For
  service functions requiring connectivity to a large number of networks, this
  approach does not scale as the number of vNICs per VM is limited and additional
  vNICs occupy additional resources on the hypervisor.

  A more scalable approach is to bind multiple networks to a single vNIC
  and let the service function, which is now shared among multiple networks,
  handle the separation of traffic itself.


* Multiple network services: A service function connects to multiple different
  network types such as a L2 network, a L3(-VPN) network, a SFC domain or
  services such as DHCP, IPAM, firewall/security, etc.


In order to achieve a flexible binding of multiple services to vNICs, a logical
separation between a vNIC (instance port) - that is, the entity that is used by
the compute service as hand-off point between the network and the VM - and a
service interface - that is, the interface a service binds to - is needed.

Furthermore, binding network services to service interfaces instead of to the
vNIC directly enables a more dynamic management of the network connectivity of
network functions as there is no need to add or remove vNICs.


Requirements
^^^^^^^^^^^^

Data model
""""""""""

The envisioned data model of the port abstraction model is as follows:

* ``instance-port``

  An instance port object represents a vNIC which is bindable to an OpenStack
  instance by the compute service (Nova).

  *Attributes:* Since an instance-port is a layer 2 device, its attributes
  include the MAC address, MTU and others (TBD).


* ``interface``

  An interface object is a logical abstraction of an instance-port. It allows to
  build hierachies of interfaces by means of a reference to a parent interface.
  Each interface represents a subset of the packets traversing a given port or
  parent interface after applying a layer 2 segmentation mechanism specific to the
  interface type.

  *Attributes:* The attributes are specific to the type of interface.

  *Examples:* trunk interface, VLAN interface, VxLAN interface, MPLS interface


* ``service``

  A service object represents a specific networking service.

  *Attributes:* The attributes of the service objects are service specific and
  valid for given service instance.

  *Examples:* L2, L3VPN, SFC


* ``service-port``

  A service port object binds an interface to a service.

  *Attributes:* The attributes of a service-port are specific for the bound
  service.

  *Examples:* port services (IPAM, DHCP, security), L2 interfaces, L3VPN
  interfaces, SFC interfaces.



Northbound API
""""""""""""""

The API for manipulating the data model is as follows:

* ``instance-port-{create,delete} <name>``

  Creates or deletes an instance port object that represents a vNIC in a VM.


* ``interface-{create,delete} <name> [interface type specific parameters]``

  Creates or deletes an interface object.


* ``service-{create,delete} <name> [service specific parameters]``

  Create a specific service object, for instance a L3VPN, a SFC domain, or a L2 network.


* ``service-port-{create,delete} <service-id> <interface-id> [service specific parameters]``

  Creates a service port object, thereby binding an interface to a given service.



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
