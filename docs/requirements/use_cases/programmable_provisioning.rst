.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Programmable Provisioning of Provider networks
----------------------------------------------
Description
~~~~~~~~~~~
In NFV environment the VNFM (consumer of OpenStack IaaS API) have no administrative
rights, however in this environment provider networks are used in some cases.
When a provider network is ceated administrative rights are needed what in the
case of non admin VNFM leeds to manual work.
It shall be possible to configure provider networks without administrative rights.
It should be possible to assign the capability to create provider networks to any roles.

Derrived Requirements
~~~~~~~~~~~~~~~~~~~~~
   - Possibility to assign the property of provider networks to any role
   - When the provider network is created it should be checked if the role of the user has the permission to create a provider network.

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
