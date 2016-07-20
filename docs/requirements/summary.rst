.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Summary and Conclusion
======================

This document presented the results of the OPNFV NetReady (Network Readiness)
project ([NETREADY]_). It described a selection of NFV-related networking use
cases and their corresponding networking requirements. Moreover, for every use
case, it describes an associated gap analysis which analyses the aforementioned
networking requirements with respect to the current OpenStack networking
architecture.

The contents of the current document are the selected use cases and their
derived requirements and identified gaps for OPNFV C release.

OPNFV NetReady is open to take any further use cases under analysis in later
OPNFV releases. The project backlog ([NETREADY-JIRA]_) lists the use cases and
topics planned to be developed in future releases of OPNFV.

Based on the gap analyses, we draw the following conclusions:

* Besides current requirements and gaps identified in support of NFV networking,
  more and more new NFV networking services are to be innovated in the near future.
  Those innovations will bring additional requirements, and more significant gaps
  will be expected. On the other hand, NFV networking business requires it
  to be made easy to innovate, quick to develop, and agile to deploy and operate.
  Therefore, a model-driven, extensible framework is expected to support NFV
  networking on-demand in order to accelerate time-to-market and achieve business
  agility for innovations in NFV networking business.

* In NFV environment it should be possible to execute network administrator tasks
  without OpenStack administrator rights.

* In a multi-site setup it should be possible to manage the connection between
  the sites in a programmable way.

The latest version of this document can be found at [SELF]_.
