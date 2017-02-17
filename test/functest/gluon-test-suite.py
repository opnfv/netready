#!/usr/bin/python

from opnfv.deployment import factory
import functest.utils.openstack_utils as osutils
import functest.utils.functest_logger as ft_logger

import json
import logging
import os
import sys
import time

logger = ft_logger.Logger("netready-gluon-vping").getLogger()
logger.setLevel(logging.DEBUG)


class GluonVPing:

    def __init__(self):
        self.controller_node = None
        self.port_ids = []
        self.vpn_id = None
        self.vpnbinding_ids = []

    def prepare_test(self):
        logger.info("Preparing Gluon vPing testcase.")

        undercloud_ip = os.getenv("INSTALLER_IP")
        handler = factory.Factory.get_handler('apex',
                                              undercloud_ip,
                                              'stack',
                                              pkey_file='/root/.ssh/id_rsa')
        nodes = handler.get_nodes()
        self.controller_node = None
        for node in nodes:
            if node.is_controller():
                self.controller_node = node
                break

        if self.controller_node is None:
            logger.error("ERROR: no controller node found.")
            raise Exception('No controller node found')

    def run(self):
        self._create_ports()
        self._create_vpn()
        self._create_vpnbinding()
        #
        # TODO boot VMs and ping
        #

    def _run_protonclient(self, options):
        cmd = "protonclient --api net-l3vpn " + options
        if self.controller_node is not None:
            logger.debug("Running command: %s" % cmd)
            output = self.controller_node.run_cmd(cmd)
            if output is None:
                raise Exception('Remote command failed')
            else:
                return output

    def _create_ports(self):
        def _build_create_port_options(name, mac, tenant_id):
            return 'port-create' \
                ' --mac_address ' + mac + \
                ' --mtu 1500' \
                ' --admin_state_up True' \
                ' --name ' + name + \
                ' --vlan_transparency True' \
                ' --vnic_type normal' \
                ' --vif_type ovs' \
                ' --status ACTIVE' \
                ' --tenant_id ' + tenant_id

        tenant_id = osutils.get_tenant_id(
                                osutils.get_keystone_client(),
                                'admin')
        for i in [1, 2]:
            options = _build_create_port_options(
                            'gluonPort' + str(i),
                            'c0:2a:14:04:43:0' + str(i),
                            tenant_id)
            output = self._run_protonclient(options)
            port_data = json.loads(output)

            logger.info('Port %s created.' % port_data['id'])
            self.port_ids.append(port_data['id'])
            time.sleep(1)

    def _create_vpn(self):
        vpn_options = 'vpn-create '\
                        '--name "GluonVPN" ' \
                        '--ipv4_family 1000:1000 ' \
                        '--ipv6_family 1000:1000 ' \
                        '--route_distinguishers 1000:1000'
        output = self._run_protonclient(vpn_options)
        vpn_data = json.loads(output)

        logger.info('VPN %s created.' % vpn_data['id'])
        self.vpn_id = vpn_data['id']
        time.sleep(1)

    def _create_vpnbinding(self):
        def _build_create_vpnbinding(port_id, counter):
            return 'vpnbinding-create' \
                    ' --interface_id ' + port_id + \
                    ' --service_id ' + self.vpn_id + \
                    ' --ipaddress 10.10.' + str(counter) + '.2' \
                    ' --subnet_prefix 24' \
                    ' --gateway 10.10.' + str(counter) + '.1'

        counter = 0
        for port_id in self.port_ids:
            options = _build_create_vpnbinding(port_id, counter)
            output = self._run_protonclient(options)
            vpnbinding_data = json.loads(output)

            logger.info('VPN-binding %s created.'
                        % vpnbinding_data['interface_id'])
            self.vpnbinding_ids.append(vpnbinding_data['interface_id'])
            counter += 1
            time.sleep(1)

    def _cleanup_ports(self):
        for port_id in self.port_ids:
            logger.info("Deleting port %s" % port_id)
            self._run_protonclient('port-delete ' + str(port_id))

    def _cleanup_vpn(self):
        logger.info("Deleting VPN %s" % self.vpn_id)
        self._run_protonclient('vpn-delete ' + str(self.vpn_id))

    def _cleanup_vpnbindings(self):
        for vpnbinding_id in self.vpnbinding_ids:
            logger.info("Deleting VPN-binding %s" % vpnbinding_id)
            self._run_protonclient('vpnbinding-delete ' + str(vpnbinding_id))

    def cleanup(self):
        logger.info("Cleaning up Gluon vPing testcase...")
        self._cleanup_vpnbindings()
        self._cleanup_vpn()
        self._cleanup_ports()


def main():
    logger.info("Running Gluon test suite...")

    try:
        gluon_vping = GluonVPing()
        gluon_vping.prepare_test()
        gluon_vping.run()
        gluon_vping.cleanup()
    except Exception as e:
        logger.info("Gluon test suite failed: %s" % e)
        return 1

    logger.info("Gluon test suite successfully completed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
