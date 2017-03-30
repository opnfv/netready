.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0

==============================
OPNFV Gluon Installation Guide
==============================

The Gluon framework can be installed by means of the :ref:`os-odl-gluon-noha
scenario <gluon-scenario>` and the Apex installer.  Please visit the :ref:`Apex
installer documentation <apex-installation>` for details on how to install the
os-odl-gluon-noha scenario in a virtual or a bare-metal environment.


Quick start guide
-----------------

The easiest way to set up Gluon is to create a virtual deployment. In a nutshell,
these are the installation steps:

 i) install a bare-metal CentOS jumphost
 ii) install the Apex RPM packages
 iii) create the virtual deployment by running the following command

.. code-block:: bash

    opnfv-deploy -v -n network_settings.yaml  \
                 -d os-odl-gluon-noha.yaml \
                 --virtual-computes 3
