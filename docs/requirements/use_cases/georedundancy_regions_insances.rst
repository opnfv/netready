.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Connection between different OpenStack regions or cloud instances
-----------------------------------------------------------------

Description
^^^^^^^^^^^
There should be an API to manage the infrastructure-s networks between two
OpenStack regions or between two OpenStack cloud instances.
(The only difference is the shared keystone in case of a region)
This capability exists in the different SDN controllers, like the Add New BGP
neighbour API of OpenDaylight. OpenStack Neutron should provide and abstracted
API for this functionality what later calls the given SDN controllers related
API.

Derrived Requirements
^^^^^^^^^^^^^^^^^^^^^
   - Possibility to define a remote and a local endpoint
   - Possiblity to define an overlay/segregation technology

Northbound API / Workflow
"""""""""""""""""""""""""
   - An infrastructure network management API is needed
   - When the endpoints are created neutron is configured to use the new network.
     (Note: Nova networking is not considered as it is deprecated.)

Data model objects
""""""""""""""""""
   - TBD

Orchestration
"""""""""""""
   - TBD

Dependencies on compute services
""""""""""""""""""""""""""""""""
   - TBD

Potential implementation
""""""""""""""""""""""""
   - TBD
