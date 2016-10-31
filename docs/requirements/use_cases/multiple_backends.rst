.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Bin Hu


Multiple Networking Backends
----------------------------

Description
^^^^^^^^^^^

Network Function Virtualization (NFV) brings the need of supporting multiple networking
back-ends in virtualized infrastructure environments.

First of all, a Service Providers' virtualized network infrastructure will consist of
multiple SDN Controllers from different vendors for obvious business reasons.
Those SDN Controllers may be managed within one cloud or multiple clouds.
Jointly, those VIMs (e.g. OpenStack instances) and SDN Controllers need to work
together in an interoperable framework to create NFV services in the Service
Providers' virtualized network infrastructure. It is needed that one VIM (e.g. OpenStack
instance) shall be able to support multiple SDN Controllers as back-end.

Secondly, a Service Providers' virtualized network infrastructure will serve multiple,
heterogeneous administrative domains, such as mobility domain, access networks,
edge domain, core networks, WAN, enterprise domain, etc. The architecture of
virtualized network infrastructure needs different types of SDN Controllers that are
specialized and targeted for specific features and requirements of those different domains.
The architectural design may also include global and local SDN Controllers.
Importantly, multiple local SDN Controllers may be managed by one VIM (e.g.
OpenStack instance).

Furthermore, even within one administrative domain, NFV services could also be quite diversified.
Specialized NFV services require specialized and dedicated SDN Controllers. Thus a Service
Provider needs to use multiple APIs and back-ends simultaneously in order to provide
users with diversified services at the same time. At the same time, for a particular NFV service,
the new networking APIs need to be agnostic of the back-ends.



Requirements
^^^^^^^^^^^^

Based on the use cases described above, we derive the following
requirements.

It is expected that in NFV networking service domain:

* One OpenStack instance shall support multiple SDN Controllers simultaneously

* New networking API shall be integrated flexibly and quickly

* New NFV Networking APIs shall be agnostic of back-ends

* Interoperability is needed among multi-vendor SDN Controllers at back-end



Current Implementation
^^^^^^^^^^^^^^^^^^^^^^

In the current implementation of OpenStack networking, SDN controllers are
hooked up to Neutron by means of dedicated plugins.  A plugin translates
requests coming in through the Neutron northbound API, e.g. the creation of a
new network, into the appropriate northbound API calls of the corresponding SDN
controller.

There are multiple different plugin mechanisms currently available in Neutron,
each targeting a different purpose. In general, there are `core plugins`,
covering basic networking functionality and `service plugins`, providing layer 3
connectivity and advanced networking services such as FWaaS or LBaaS.



Core and ML2 Plugins
''''''''''''''''''''

The Neutron core plugins cover basic Neutron functionality, such as creating
networks and ports. Every core plugin implements the functionality needed to
cover the full range of the Neutron core API. A special instance of a core
plugin is the ML2 core plugin, which in turn allows for using sub-drivers -
separated again into type drivers (VLAN, VxLAN, GRE) or mechanism drivers (OVS,
OpenDaylight, etc.). This allows to using dedicated sub-drivers for dedicated
functionality.

In practice, different SDN controllers use both plugin mechanisms to integrate
with Neutron. For instance OpenDaylight uses a ML2 mechanism plugin driver
whereas OpenContrail integrated by means of a full core plugin.

In its current implementation, only one Neutron core plugin can be active at any
given time. This means that if a SDN controller utilizes a dedicated core
plugin, no other SDN controller can be used at the same time for the same type
of service.

In contrast, the ML2 plugin allows for using multiple mechanism drivers
simultaneously. In principle, this enables a parallel deployment of multiple SDN
controllers if and only if all SDN controllers integrate through a ML2 mechanism
driver.



Neutron Service Plugins
'''''''''''''''''''''''

Neutron service plugins target L3 services and advanced networking services,
such as BGPVPN or LBaaS. Typically, a service itself provides a driver plugin
mechanism which needs to be implemented for every SDN controller. As the
architecture of the driver mechanism is up to the community developing the
service plugin, it needs to be analyzed for every driver plugin mechanism
individually if and how multiple back-ends are supported.



Gaps in the current solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given the use case description and the current implementation of OpenStack
Neutron, we identify the following gaps:


* **[MB-GAP1] Limited support for multiple back-ends**

  As pointed out above, the Neutron core plugin mechanism only allows for one
  active plugin at a time. The ML2 plugin allows for running multiple mechanism
  drivers in parallel, however, successful inter-working strongly depends on the
  individual driver.

  Moreover, the ML2 plugin and its API is - by design - very layer 2 focused. For
  NFV networking use cases beyond layer 2, for instance L3VPNs, a more flexible
  API is required.


Conclusion
^^^^^^^^^^

We conclude that a complementary method of integrating multiple SDN controllers
into a single OpenStack deployment is needed to fulfill the needs of operators.
