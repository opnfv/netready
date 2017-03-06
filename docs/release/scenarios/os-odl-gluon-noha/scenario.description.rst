.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) <optionally add copywriters name>

=======================
OPNFV os-odl-gluon-noha
=======================

This document provides scenario level details for the Danube release of Gluon.

.. contents::
   :depth: 3
   :local:

Introduction
------------
.. In this section explain the purpose of the scenario and the types of capabilities provided

This scenario integrates the Gluon framework into the OPNFV platform and makes
it available for testing and development. Gluon is a model-driven networking
framework that extends OpenStack Neutron with the ability to generate new
networking APIs from YAML models. Additionally, Gluon provides a mechanism for
integrating multiple networking backends (SDN controllers) in parallel.


Scenario components and composition
-----------------------------------
.. In this section describe the unique components that make up the scenario,
.. what each component provides and why it has been included in order
.. to communicate to the user the capabilities available in this scenario.

The scenario contains Gluon 1.0.2 which was released in conjunction with
OpenStack Ocata. However, Gluon 1.0.2 is fully compatible with OpenStack Newton
which is used in the Danube release of OPNFV and hence also in this scenario.

The Gluon framework consists of five software components:

* **Gluon core plugin:** Gluon integrates into OpenStack Neutron as an extended
  version of the existing ML2 core plugin. It hence runs in the context of the
  Neutron server process on the OpenStack controller nodes.

* **Proton server:** The proton server runs one or more Protons which expose
  service-specific REST APIs. This scenario currently only contains a single
  Proton, exposing a L3VPN service API.

* **Proton client:** For every API model, the protonclient tool generates
  the corresponding command line options for creating, deleting and updating
  the API objects exposed by a Proton.

* **etcd:** Gluon and all Protons maintain their state in the distributed
  key-value store etcd.

* **Shim layer for OpenDaylight:** This shim layer is notified about changes
  in the configuration state of a Proton and translates these changes into API
  calls to the OpenDaylight SDN controller. This scenario contains a shim layer
  for the L3VPN Proton API.

In addition to these scenario-specific components, the scenario contains
OpenStack Newton and OpenDaylight Boron.


Scenario usage overview
-----------------------
.. Provide a brief overview on how to use the scenario and the features available to the
.. user.  This should be an "introduction" to the user guide document, and explicitly link to it,
.. where the specifics of the features are covered including examples and API's

The Gluon framework extends existing Neutron functionality by exposing an
alternative L3VPN API through a corresponding Proton. As a result, the existing
Neutron functionality remains available as for any other scenario with
OpenDaylight.

The configuration of the L3VPN service is done throught the RESTful API exposed
by the L3VPN proton or by means of the protonclient.  The high-level workflow
for configuring the L3VPN service Proton is as follows:

  i) create a new port
  ii) create a new vpn object
  iii) bind the port to the vpn object

More detailed information can be found in the `Gluon feature guide <../release_userguide/index.html>`_.


Limitations, Issues and Workarounds
-----------------------------------
.. Explain scenario limitations here, this should be at a design level rather than discussing
.. faults or bugs.  If the system design only provide some expected functionality then provide
.. some insight at this point.

The following limitations apply:

* The OpenDaylight shim layer currently supports only a single L3VPN.

* The DHCP service is not enabled for VMs connecting to a L3VPN created through
  Gluon. Hence, VMs need to be configured with static IP addresses.

