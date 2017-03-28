.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

=================================
Gluon Post Installation Procedure
=================================

.. Add a brief introduction to the methods of validating the installation
.. according to this specific installer or feature.

The configuration of the Gluon framework is entirely handled by the
corresponding scenario os-odl-gluon-noha available for the Apex installer. In
general, Apex installs and configures all components so that no additional
configuration steps are needed after deploying the aforementioned scenario.


Automated post installation activities
--------------------------------------

.. Describe specific post installation activities performed by the OPNFV
.. deployment pipeline including testing activities and reports. Refer to
.. the relevant testing guides, results, and release notes.

.. note: this section should be singular and derived from the test projects
.. once we have one test suite to run for all deploy tools.  This is not the
.. case yet so each deploy tool will need to provide (hopefully very simillar)
.. documentation of this.

An overview of all test suites run by the OPNFV pipeline against the
os-odl-gluon-noha scenario as well as the test results can be found at the
`Functest test result overview page.
<http://testresults.opnfv.org/reporting/functest/release/danube/index-status-apex.html>`_



Gluon post configuration procedures
--------------------------------------

.. Describe any deploy tool or feature specific scripts, tests or procedures
.. that should be carried out on the deployment post install and configuration
.. in this section.

No post configuration procedures need to be performed after deploying the
os-odl-gluon-noha scenario using the Apex installer.



Platform components validation
------------------------------

.. Describe any component specific validation procedures necessary for your
.. deployment tool in this section.

As described in the :ref:`Gluon scenario description <gluon-scenario>`, the
Gluon framework consists of five software components. This section describes
how to validate their successful installation.

* **Gluon core plugin**: Check in the file ``/etc/neutron/neutron.conf`` that
  the Neutron core plugin is set to ``gluon``.

* **Proton server**: Check that the process ``proton-server`` is running.

* **Proton client**: Verify that the ``protonclient`` tool is installed and
  executable.

* **etcd**: Verify that the etcd key-value-store is installed and running by
  means of the etcdctl tool.

* **Proton shim layer for OpenDaylight**: Verify that the
  ``proton-shim-server`` process is running.
