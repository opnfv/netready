.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Georedundancy Use cases (Draft)
===============================
Connection between different OpenStack cells
--------------------------------------------
Description
~~~~~~~~~~~
There should be an API to manage the infrastructure-s networks between two OpenStack cells.
(Note: In the Mitaka release of OpenStack cells v1 are considered as, cells v2 functionaity is under implementation)

Derrived Requirements
~~~~~~~~~~~~~~~~~~~~~
   - Possibility to define a remote and a local endpoint
   - Possiblity to define an overlay/segregation technology
   - As in case of cells the nova-api service is shared it should be possible to identify the cell in the API calls

Northbound API / Workflow
+++++++++++++++++++++++++
   - An infrastructure network management API is needed
   - When the endpoints are created neutron is configured to use the new network. (Note: Nova networking is not considered as it is deprecated.)


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

Connection between different OpenStack regions or cloud instances
-----------------------------------------------------------------

Description
~~~~~~~~~~~
There should be an API to manage the infrastructure-s networks between two OpenStack regions or between two OpenStack cloud instances.
(The only difference is the shared keystone in case of a region)

Derrived Requirements
~~~~~~~~~~~~~~~~~~~~~
   - Possibility to define a remote and a local endpoint
   - Possiblity to define an overlay/segregation technology

Northbound API / Workflow
+++++++++++++++++++++++++
   - An infrastructure network management API is needed
   - When the endpoints are created neutron is configured to use the new network. (Note: Nova networking is not considered as it is deprecated.)


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

