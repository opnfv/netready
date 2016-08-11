.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

***************************
NetReady: Network Readiness
***************************

:Project: NetReady, https://wiki.opnfv.org/display/netready/NetReady
:Editors: Georg Kunz (Ericsson)
:Authors: Bin Hu (AT&T), Gergely Csatari (Nokia), Georg Kunz (Ericsson) and
          others

:Abstract: OPNFV provides an infrastructure with different SDN controller
           options to realize NFV functionality on the platform it builds. As
           OPNFV uses OpenStack as a VIM, we need to analyze the capabilities
           this component offers us. The networking functionality is provided
           by a component called Neutron, which provides a pluggable
           architecture and specific APIs for integrating different networking
           backends, for instance SDN controllers. As NFV wasn't taken into
           consideration at the time when Neutron was designed we are already
           facing several bottlenecks and architectural shortcomings while
           implementing NFV use cases.

           The NetReady project aims at evolving OpenStack networking
           step-by-step to find the most efficient way to fulfill the
           requirements of the identified NFV use cases, taking into account the
           NFV mindset and the capabilities of SDN controllers.

:History:

           ========== =====================================================
           Date       Description
           ========== =====================================================
           22.03.2016 Project creation
           19.04.2016 Initial version of the deliverable uploaded to Gerrit
           22.07.2016 First version ready for sharing with the community
           22.09.2016 Version accompanying the OPNFV Colorado release
           ========== =====================================================

.. raw:: latex

    \newpage

.. include::
    glossary.rst

.. toctree::
    :maxdepth: 4
    :numbered:

    introduction.rst
    use_cases.rst
    summary.rst
    references.rst
