.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Connection between different OpenStack cells
--------------------------------------------
Description
^^^^^^^^^^^
There should be an API to manage the infrastructure-s networks between two
OpenStack cells.
(Note: In the Mitaka release of OpenStack cells v1 are considered as, cells v2
functionaity is under implementation)
This capability exists in the different SDN controllers, like the Add New BGP
neighbour API of OpenDaylight. OpenStack Neutron should provide and abstracted
API for this functionality what later calls the given SDN controllers related
API.

Derrived Requirements
^^^^^^^^^^^^^^^^^^^^^
   - Possibility to define a remote and a local endpoint
   - As in case of cells the nova-api service is shared it should be possible
     to identify the cell in the API calls

Northbound API
""""""""""""""
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
   None.

Potential implementation
""""""""""""""""""""""""
   - TBD
