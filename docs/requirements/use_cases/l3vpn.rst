.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) Bin Hu

L3VPN Use Cases
===============

.. toctree::
   l3vpn_any_to_any.rst
   l3vpn_ecmp.rst
   l3vpn_hub_and_spoke.rst


Conclusion
----------

Based on the gap analyses of the three specific L3VPN use cases we conclude that
there are gaps in both the functionality provided by the BGPVPN project as well
as the support for multiple backends in Neutron.

Some of the identified gaps [L3VPN-ECMP-GAP1, L3VPN-ECMP-GAP2, L3VPN-HS-GAP3]
in the BGPVPN project are merely missing functionality which can be integrated
in the existing OpenStack networking architecture.

Other gaps, such as the inability to explicitly disable the layer 2 semantics of
Neutron networks [L3VPN-HS-GAP1] or the tight integration of ports and networks
[L3VPN-HS-GAP2] hinder a clean integration of the needed functionality. In order
to close these gaps, fundamental changes in Neutron or alternative approaches
need to be investigated.
