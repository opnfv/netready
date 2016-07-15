.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Bin Hu

Network Function Virtualization (NFV) brings the need of supporting multiple networking
back-ends in virtualized infrastructure environment.

First of all, a Service Providers' virtualized network infrastructure will consist of
multiple SDN Controllers from different vendors for obvious business reason.
Those SDN Controllers may be managed within one cloud or multiple clouds.
Jointly, those VIMs (e.g. OpenStack instances) and SDN Controllers need to work
together in an interoperable framework to create NFV services in the Service
Providers' virtualized network infrastructure. It is needed that one VIM (e.g. OpenStack
instance) shall be able to support multiple SDN Controllers at back-end.

Secondly, a Service Providers' virtualized network infrastructure will serve multiple,
heterogeneous administrative domains, such as mobility domain, access networks,
edge domain, core networks, WAN, enterprise domain, etc. The architecture of
virtualized network infrastructure needs different types of SDN Controllers that are
specialized and targeted for specific features and requirements of those different domains.
The architectural design may also include global and local SDN Controllers. And multiple
local SDN Controllers may be managed by one VIM (e.g. OpenStack instance).

Furthermore, even within one administrative domain, NFV services could also be quite diversified.
Specialized NFV service needs specialized and dedicated SDN Controller too. Thus a Service
Provider needs to use multiple APIs and back-ends simultaneously in order to provide
users with diversified services at the same time. At the same time, for a particular NFV service,
the new networking APIs need to be agnostic of the back-ends.

Therefore, it is expected that in NFV networking service domain:

* One OpenStack instance shall support multiple APIs and SDN Controllers simultaneously

* Interoperability is needed among multi-vendor SDN Controllers at back-end

* New NFV Networking APIs  shall be agnostic of back-ends

