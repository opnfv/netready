.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Georedundancy: Connection between different OpenStack cells
-----------------------------------------------------------
Georedundancy refers to a configuration which ensures the service continuity of
the VNF-s even if a whole datacenter fails [Q: Do we include or exclude VNF
pooling?].

This can be achieved by redundant VNF-s in a hot (spare VNF is running its
configuration and internal state is synchronised to the active VNF),
warm (spare VNF is running, its configuration is synchronised to the active VNF)
or cold (spare VNF is not running, active VNF-s configuration is stored in a
database and dropped to the spare VNF during its activation) standby state in a
different datacenter from where the active VNF-s are running.
The synchronisation and data transfer can be handled by the application or the infrastructure.
In all of these georedundancy setups there is a need for a network connection
between the datacenter running the active VNF and the datacenter running the
spare VNF.

In case of a distributed cloud it is possible that the georedundant cloud of an application
is not predefined or changed and the change requires configuration in the underlay networks.

This set of georedundancy use cases is about enabling the possiblity to select a datacenter as
backup datacenter and build the connectivity between the NFVI-s in the
different datacenters in a programmable way.

As an example the following picture (:numref:`georedundancy-before`) shows a
multicell cloud setup where the underlay network is not fully mashed.

.. figure:: images/georedundancy-before.png
    :name:  georedundancy-before
    :width: 25%

Each datacenter (DC) is a separate OpenStack cell, region or instance. Let's
assume that a new VNF is started in DC b with a Redundant VNF in DC d. In this
case a direct underlay network connection is needed between DC b and DC d. The
configuration of this connection should be programable in both DC b and DC d.
The result of the deployment is shown in the following figure
(:numref:`georedundancy-after`):

.. figure:: images/georedundancy-after.png
   :name:  georedundancy-after
   :width: 25%

Description
^^^^^^^^^^^
There should be an API to manage the infrastructure-s networks between two
OpenStack cells.
(Note: In the Mitaka release of OpenStack cells v1 are considered as, cells v2
functionaity is under implementation)

- Maybe the existing capability of Neutron to have several subnets associated
  to an external network is enough?

Requirements
^^^^^^^^^^^^
   - Possibility to define a remote and a local endpoint
   - As in case of cells the nova-api service is shared it should be possible
     to identify the cell in the API calls

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
   None.

Potential implementation
""""""""""""""""""""""""
   - TBD
