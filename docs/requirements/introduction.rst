.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Introduction
============

This document represents and describes the results of the OPNFV NetReady
(Network Readiness) project. Specifically, the document comprises a selection of
NFV-related networking use cases and their networking requirements. For every
use case, it furthermore presents a gap analysis of the aforementioned
requirements with respect to the current OpenStack networking architecture.
Finally it provides a description of potential solutions and improvements.


Scope
-----

NetReady is a project within the OPNFV initiative. Its focus is on NFV (Network
Function Virtualization) related networking use cases and their requirements on
the underlying NFVI (Network Function Virtualization Infrastructure).

The NetReady project addresses the OpenStack networking architecture,
specifically OpenStack Neutron, from a NFV perspective. Its goal is to identify
gaps in the current OpenStack networking architecture with respect to NFV
requirements and to propose and evaluate improvements and potential complementary
solutions.


Problem Description
-------------------

Telco ecosystem's movement towards the cloud domain results in Network Function
Virtualization that is discussed and specified in ETSI NFV. This movement opens
up many green field areas which are full of potential growth in both business
and technology. This new NFV domain brings new business opportunities and new
market segments as well as emerging technologies that are exploratory and
experimental in nature, especially in NFV networking.

It is often stated that NFV imposes additional requirements on the networking
architecture and feature set of the underlying NFVI beyond those of data center
networking. For instance, the NFVI needs to establish and manage connectivity
beyond the data center to the WAN (Wide Area Network). Moreover, NFV networking
use cases often abstract from L2 connectivity and instead focus on L3-only
connectivity. Hence, the NFVI networking architecture needs to be flexible
enough to be able to meet the requirements of NFV-related use cases in addition
to traditional data center networking.

Traditionally, OpenStack networking, represented typically by the OpenStack
Neutron project, targets virtualized data center networking. This comprises
originally establishing and managing layer 2 network connectivity among VMs
(Virtual Machines). Over the past releases of OpenStack, Neutron has grown to
provide an extensive feature set, covering both L2 as well as L3 networking
services such as virtual routers, NATing, VPNaaS and BGP VPNs.

It is an ongoing debate how well the current OpenStack networking architecture
can meet the additional requirements of NFV networking. Hence, a thorough
analysis of NFV networking requirements and their relation to the OpenStack
networking architecture is needed.

Besides current additional use cases and requirements of NFV networking,
more importantly, because of the **green field** nature of NFV, it is foreseen
that there will be more and more new NFV networking use cases and services,
which will bring new business, in near future. The challenges for telco ecosystem
are to:

- Quickly catch the new business opportunity;

- Execute it in agile way so that we can accelerate the time-to-market and improve
  the business agility in offering our customers with innovative NFV services.

Therefore, it is critically important for telco ecosystem to quickly develop and deploy
new NFV networking APIs on-demand based on market need.

Goals
-----

The goals of the NetReady project and correspondingly this document are the
following:

- This document comprises a collection of relevant NFV networking use cases and
  clearly describes their requirements on the NFVI. These requirements are
  stated independently of a particular implementation, for instance OpenStack
  Neutron. Instead, requirements are formulated in terms of APIs (Application
  Programming Interfaces) and data models needed to realize a given NFV use
  case.

- The list of use cases is not considered to be all-encompassing but it
  represents a carefully selected set of use cases that are considered to be
  relevant at the time of writing. More use cases may be added over time. The
  authors are very open to suggestions, reviews, clarifications, corrections
  and feedback in general.

- This document contains a thorough analysis of the gaps in the current
  OpenStack networking architecture with respect to the requirements imposed
  by the selected NFV use cases. To this end, we analyze existing functionality
  in OpenStack networking.

- Beyond current list of use cases and gap analysis in the document, more importantly,
  it is the future of NFV networking that needs to be made easy to innovate, quick to
  develop, and agile to deploy and operate. A model-driven, extensible framework
  is expected to achieve agility for innovations in NFV networking.

- This document will in future revisions describe the proposed improvements
  and complementary solutions needed to enable OpenStack to fulfill the
  identified NFV requirements.

