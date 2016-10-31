.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

Programmable Provisioning of Provider Networks
----------------------------------------------
Description
~~~~~~~~~~~

In a NFV environment the VNFMs (Virtual Network Function Manager) are consumers
of the OpenStack IaaS API. They are often deployed without administrative rights
on top of the NFVI platform. Furthermore, in the telco domain provider networks
are often used. However, when a provider network is created administrative
rights are needed what in the case of a VNFM without administrative rights
requires additional manual configuration work.  It shall be possible to
configure provider networks without administrative rights.  It should be
possible to assign the capability to create provider networks to any roles.

The following figure (:numref:`api-users`) shows the possible users of an
OpenStack API and the relation of OpenStack and ETSI NFV components. Boxes with
solid line are the ETSI NFV components while the boxes with broken line are the
OpenStack components.

.. figure:: images/api-users.png
    :name:  api-users
    :width: 50%


Requirements
~~~~~~~~~~~~
   - Authorize the possibility of provider network creation based on policy
   - There should be a new entry in :code:`policy.json` which controls the
     provider network creation
   - Default policy of this new entry should be :code:`rule:admin_or_owner`.
   - This policy should be respected by the Neutron API

Northbound API / Workflow
+++++++++++++++++++++++++
   - No changes in the API

Data model objects
++++++++++++++++++
   - No changes in the data model


Current implementation
~~~~~~~~~~~~~~~~~~~~~~
Only admin users can manage provider networks [OS-NETWORKING-GUIDE-ML2]_.


Potential implementation
~~~~~~~~~~~~~~~~~~~~~~~~
   - Policy engine shall be able to handle a new provider network creation and
     modification related policy.
   - When a provider network is created or modified neutron should check the
     authority with the policy engine instead of requesting administrative
     rights.


Solution in upstream community
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A bug report has been submitted to the upstream OpenStack community to highlight
this gap:
https://bugs.launchpad.net/neutron/+bug/1630880

This bug report revealed that this use case has already been addressed in the
upstream community. Specifically, it is possible to specify the roles (e.g.,
admin, regular user) in the Neutron policy.json file which are able to create
and update provider networks.

However, the OpenStack user guide wrongly stated that **only** administrators
can create and update provider type networks. Hence, a correction has been
submitted to the OpenStack documentation repository, clarifying the possibility
to change this behavior based on policies:
https://review.openstack.org/#/c/390359/

In conclusion, this use case has been retired as the corresponding gaps have been
closed in the upstream community.
