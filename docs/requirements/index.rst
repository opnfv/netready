.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

***************************
NetReady: Network Readiness
***************************

:Project: NetReady, https://wiki.opnfv.org/display/netready/NetReady

:Abstract: OPNFV provides an infrastructure with different SDN controller
           options to realize NFV functionality on the platform it builds. As
           OPNFV uses OpenStack as VIM, we need to analyze the capabilities this
           component offers us. The networking functionality is provided by a
           single component called Neutron, which hides the controller under it,
           let it be Neutron itself or any supported SDN controller. As NFV
           wasn't taken into consideration at the time when Neutron was designed
           we are already facing several bottlenecks and architectural
           shortcomings while implementing our use cases.

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
    current_solutions.rst
    gap_analysis.rst
    architecture.rst
    implementation.rst
    summary.rst
