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
   - Authorize the possibility of provider network creation based on policy
   - There should be a new entry in :code:`policy.json` which controls the provider network creation
   - Default policy of this new enrty should be :code:`rule:admin_or_owner`.

Northbound API / Workflow
+++++++++++++++++++++++++
   - No changes in the API

Data model objects
++++++++++++++++++
   - No changes in the data model

Orchestration
+++++++++++++
   - TBD

Dependencies on compute services
++++++++++++++++++++++++++++++++
   - TBD

Potential implementation
++++++++++++++++++++++++
   - Policy engine shall be able to handle a new provider network creation and modification related policy
   - When a provider network is created or modified neutron should check the authority with the policy engine instead of requesting administrative rights
