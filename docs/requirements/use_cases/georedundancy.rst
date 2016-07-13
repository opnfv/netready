.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Georedundancy
=============
Georedundancy refers to a configuration which ensures the service continuity of
the VNF-s even if a whole datacenter fails.

It is possible that the VNF application layer provides additional redundancy
with VNF pooling on top of the georedundancy functionality described here.

It is possible that either the VNFC-s of a single VNF are spread across several
datacenters (this case is covered by the OPNFV multisite project [MULTISITE]_
or different, redundant VNF-s are started in different datacenters.

When the different VNF-s are started in different datacenters the redundancy
can be achieved by redundant VNF-s in a hot (spare VNF is running its
configuration and internal state is synchronised to the active VNF),
warm (spare VNF is running, its configuration is synchronised to the active VNF)
or cold (spare VNF is not running, active VNF-s configuration is stored in a
persistent, central store and configured to the spare VNF during its activation)
standby state in a different datacenter from where the active VNF-s are running.
The synchronisation and data transfer can be handled by the application or by
the infrastructure.

In all of these georedundancy setups there is a need for a network connection
between the datacenter running the active VNF and the datacenter running the
spare VNF.

In case of a distributed cloud it is possible that the georedundant cloud of an
application is not predefined or changed and the change requires configuration
in the underlay networks when the network operator uses network isolation.
Isolation of the traffic between the datacenters might be needed due to the
multitenant usage of NFVI/VIM or due to the IP pool management of the network
operator.

This set of georedundancy use cases is about enabling the possiblity to select a
datacenter as backup datacenter and build the connectivity between the NFVI-s in
the different datacenters in a programmable way.

The focus of these uses cases is on the functionality of OpenStack it is not
considered how the provisioning of physical resources is handled by the SDN
controllers to interconnect the two datacenters.

As an example the following picture (:numref:`georedundancy-before`) shows a
multicell cloud setup where the underlay network is not fully meshed.

.. figure:: images/georedundancy-before.png
    :name:  georedundancy-before
    :width: 50%

Each datacenter (DC) is a separate OpenStack cell, region or instance. Let's
assume that a new VNF is started in DC b with a Redundant VNF in DC d. In this
case a direct underlay network connection is needed between DC b and DC d. The
configuration of this connection should be programable in both DC b and DC d.
The result of the deployment is shown in the following figure
(:numref:`georedundancy-after`):

.. figure:: images/georedundancy-after.png
   :name:  georedundancy-after
   :width: 50%

.. toctree::
   georedundancy_cells.rst
   georedundancy_regions_insances.rst

Conclusion
----------
  An API is needed what provides possibility to set up the local and remote
  endpoints for the underlay network. This API present in the SDN solutions, but
  OpenStack does not provides and abstracted API for this functionality to hide
  the differences of the SDN solutions.
