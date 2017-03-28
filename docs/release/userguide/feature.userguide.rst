.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) <optionally add copywriters name>

=========================
OPNFV NetReady User Guide
=========================

.. contents::
   :depth: 3
   :local:

Gluon Description
-----------------

**Gluon** brings a Networking Service Framework that enables Telecom Service
Providers to provide their customers with networking services on-demand.
**Gluon** uses a model-driven approach to generate Networking Service APIs
(including objects, database schema, and RESTful API endpoints) from a YAML
file which models the Networking Service. When a Telecom Service Provider
needs to launch a new Networking Service, it only needs to model the new
service in a YAML file. The **Gluon** framework generates the APIs accordingly.
Thus **Gluon** helps Telecom Service Providers accelerate the time-to-market
and achieve business agility through its extensibility and scalability in
generating APIs for new use-cases and services.

Gluon Capabilities and Usage
----------------------------

**Gluon** is the port arbiter that maintains a list of ports and bindings of
different networking backends. A **Proton** is a set of APIs of a particular
NFV Networking Service. A **Proton Server** is the API server that hosts
multiple **Protons**, i.e. multiple sets of APIs. **Gluon** uses backend
drivers to interact with the **Proton Server** for port binding and other
operations.

A **Proton** is created by a **Particle Generator** based on a YAML file modeled
for this particular NFV Networking Service. When a **Proton** is created, the
objects, database schema, and RESTful APIs of this **Proton** are created.
Then the **Proton** specific driver would be loaded into **Gluon**.

When the **Proton Server** receives port binding and other operation requests,
it broadcasts those requests to ``etcd``. The **Shim Layers** of respective
SDN Controllers listen to ``etcd``, and get the notification from ``etcd``.
Based on the type of operations, parameter data, and its own deployment and
policy configuration, SDN Controllers act upon accordingly. This mechanism is
similar to Neutron's Hierarchical Port Binding (HPB), and provides the
flexibility and scalability when a port operation needs to be supported by
multiple SDN Controllers in collaborative and interoperable way.

Gluon API Guidelines and Examples
---------------------------------

This section shows you how to use **Proton** to create the needed objects, and
then use ``nova boot`` to bind the port to a VM. It is assumed that you have
already installed Gluon package, including ``etcd`` and **Gluon Plugin**, and
started **Proton Server**.  If not, please refer to the :ref:`Installation guide
<netready-installation>`.

Getting Help
~~~~~~~~~~~~

Just typing the ``protonclient --help`` command gives you general help
information:

.. code-block:: bash

    $ protonclient --help

    Usage: protonclient --api <api_name> [OPTIONS] COMMAND[ARGS]...

    Options:
    --api TEXT      Name of API, one of ['net-l3vpn', 'test']
    --port INTEGER  Port of endpoint (OS_PROTON_PORT)
    --host TEXT     Host of endpoint (OS_PROTON_HOST)
    --help          Show this message and exit.

Mandatory Parameters
~~~~~~~~~~~~~~~~~~~~

``--api <api_name>`` is a mandatory parameter. For example, ``--api net-l3vpn``.

Just typing the ``protonclient`` command shows you that those mandatory
parameters are required, and gives you general help information too.

.. code-block:: bash

    $ protonclient
    --api is not specified!

    Usage: protonclient --api <api_name> [OPTIONS] COMMAND[ARGS]...

    Options:
    --api TEXT      Name of API, one of ['net-l3vpn', 'test']
    --port INTEGER  Port of endpoint (OS_PROTON_PORT)
    --host TEXT     Host of endpoint (OS_PROTON_HOST)
    --help          Show this message and exit.

Using L3VPN Proton
~~~~~~~~~~~~~~~~~~

**NOTE** that there is a KNOWN BUG in the **Usage** message where the mandatory
parameters ``--api net-l3vpn`` are missing.

.. code-block:: bash

    $ protonclient --api net-l3vpn
    Usage: protonclient [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      interface-create
      interface-delete
      interface-list
      interface-show
      interface-update
      port-create
      port-delete
      port-list
      port-show
      port-update
      vpn-create
      vpn-delete
      vpn-list
      vpn-show
      vpn-update
      vpnafconfig-create
      vpnafconfig-delete
      vpnafconfig-list
      vpnafconfig-show
      vpnafconfig-update
      vpnbinding-create
      vpnbinding-delete
      vpnbinding-list
      vpnbinding-show
      vpnbinding-update

The following sections give you the general work flow of how to use Proton to
create and configure an L3VPN.

For more details and examples, please refer to the `Gluon upstream user guide
<https://github.com/openstack/gluon/blob/master/doc/source/usage.rst>`_.

Work Flow of Using L3VPN
++++++++++++++++++++++++

The work flow of using L3VPN includes:

* **Step 1: Create ``Port`` Object**

.. code-block:: bash

    $ protonclient --api net-l3vpn port-create --help
    $ protonclient --api net-l3vpn port-create [ARGS] ...

Please **NOTE**: a default ``interface`` object is automatically created too
when a ``Port`` is created, and this default ``interface`` object is attached
to this ``Port`` object. The UUID of this default ``Interface`` object
will be the same as the UUID of the parent ``Port`` object.

* **Step 2 (Optional): Create ``Interface`` Object**

.. code-block:: bash

    $ protonclient --api net-l3vpn interface-create --help
    $ protonclient --api net-l3vpn interface-create [ARGS] ...

Please **NOTE**: This step is optional because a default ``Interface`` object
was already automatically created when a ``Port`` object was created at
**Step 1**.

  * **For example: list the default ``Interface`` Object**:

.. code-block:: bash

    $ protonclient --api net-l3vpn interface-list

* **Step 3 (Optional): Create ``VPNAFConfig`` Object**

.. code-block:: bash

    $ protonclient --api net-l3vpn vpnafconfig-create --help
    $ protonclient --api net-l3vpn vpnafconfig-create [ARGS] ...

Please **NOTE**: This step is optional because all parameters needed for an
L3VPN (route specifiers) are also present in creating a ``VPN`` service object
at **Step 4**. This part of the API needs to be aligned in the future.

* **Step 4: Create ``VPN`` Object**

.. code-block:: bash

    $ protonclient --api net-l3vpn vpn-create --help
    $ protonclient --api net-l3vpn vpn-create [ARGS] ...

At this point you have a ``Port`` object, default ``Interface`` object and a
``VPN`` service object created.

  * View ``VPN`` and ``Port`` Objects

You can view the values with the following commands:

.. code-block:: bash

    $ protonclient --api net-l3vpn vpn-list
    $ protonclient --api net-l3vpn port-list

* **Step 5: Create ``VPNBinding`` Object**

You need to create a ``VPNBinding`` object to tie the ``Interface`` and the
``Service`` together in order to achieve service binding.

.. code-block:: bash

    $ protonclient --api net-l3vpn vpnbinding-create --help
    $ protonclient --api net-l3vpn vpnbinding-create [ARGS] ...

  * View ``VPNBinding`` Objects

.. code-block:: bash

    $ protonclient --api net-l3vpn vpnbinding-list

At this point you have had all of the information needed for an L3VPN Port in
Proton.

* **Step 6: Create VM and Bind our L3VPN Port**

.. code-block:: bash

    $ nova --debug boot --flavor 1 --image cirros --nic port-id=<port-id> <VM-Name>

To Use Gluon in a Project
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    import gluon

