.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Connection between different OpenStack cells
--------------------------------------------
Description
~~~~~~~~~~~
There should be an API to manage the infrastructure-s networks between two
OpenStack cells. (Note: In the Mitaka release of OpenStack cells v1 are
considered as experimental, while cells v2 functionality is under
implementation). Cells are considered to be problematic from maintainability
perspective as the sub-cells are using only the internal message bus and there
is no API (and CLI) to do maintenance actions in case of a network connectivity
problem between the main cell and the sub cells.

The functionality behind the API depends on the underlying network providers (SDN
controllers) and the networking setup.
(For example OpenDaylight has an API to add new BGP neighbour.)

OpenStack Neutron should provide an abstracted API for this functionality what
calls the underlying SDN controllers API.

Derrived Requirements
~~~~~~~~~~~~~~~~~~~~~
   - Possibility to define a remote and a local endpoint
   - As in case of cells the nova-api service is shared it should be possible
     to identify the cell in the API calls

Northbound API / Workflow
+++++++++++++++++++++++++
   - An infrastructure network management API is needed
   - API call to define the remote and local infrastructure endpoints
   - When the endpoints are created neutron is configured to use the new network.

Dependencies on compute services
++++++++++++++++++++++++++++++++
   None.

Data model objects
++++++++++++++++++
   - local and remote endpoint objects (Most probably IP addresses with some
   additional properties).

Current implementation
~~~~~~~~~~~~~~~~~~~~~~
  Current OpenStack implementation provides no way to set up the underlay
  network connection.
  OpenStack Tricicle project [TRICICLE]_
  has plans to build up inter datacenter L2 and L3 networks.

Gaps in the current solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  An infrastructure management API is missing from Neutron where the local and
  remote endpoints of the underlay network could be configured.
