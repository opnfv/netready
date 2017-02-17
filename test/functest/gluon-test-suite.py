#!/usr/bin/python

from opnfv.deployment import factory
import functest.utils.openstack_utils as osutils
import functest.utils.functest_logger as ft_logger
from functest.utils.constants import CONST

import json
import logging
import os
import sys
import time

logger = ft_logger.Logger('netready-gluon-vping').getLogger()
logger.setLevel(logging.DEBUG)


class GluonVPing:

    def __init__(self):
        self.controller_node = None
        self.port_ids = []
        self.vpn_id = None
        self.vpnbinding_ids = []
        self.novaclient = osutils.get_nova_client()
        self.neutronclient = osutils.get_neutron_client()
        self.image_id = None
        self.flavor_id = None
        self.instance_1 = None
        self.instance_2 = None
        self.vm_boot_timeout = 180

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
        self._prepare_image()
        self._prepare_flavor()
        self._create_ports()
        self._create_vpn()
        self._create_vpnbinding()
        self._boot_vms()

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
            options = _build_create_port_options('gluonPort' + str(i),
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
        self._cleanup_instances()
        self._cleanup_vpnbindings()
        self._cleanup_vpn()
        self._cleanup_ports()
        self._cleanup_image()
        self._cleanup_flavor()

    def _prepare_image(self):
        image_name = 'gluon-test-image'
        self.image_id = osutils.get_image_id(osutils.get_glance_client(),
                                             image_name)
        if self.image_id == '':
            image_filename = CONST.openstack_image_file_name
            image_format = CONST.openstack_image_disk_format
            image_path = '{0}/{1}'.format(CONST.dir_functest_data,
                                          image_filename)

            logger.info('Creating Glance image.')
            self.image_id = \
                osutils.create_glance_image(osutils.get_glance_client(),
                                            image_name,
                                            image_path,
                                            image_format,
                                            container='bare',
                                            public='public')
            if self.image_id is None:
                raise Exception('Glance image creation failed')
        else:
            logger.info('Test image %s already exists' % image_name)

    def _cleanup_image(self):
        logger.info('Deleting Glance image.')
        if not osutils.delete_glance_image(self.novaclient, self.image_id):
            raise Exception('Image deletion failed.')

    def _prepare_flavor(self):
        logger.info('Creating Nova flavor.')
        self.flavor_id = osutils.get_flavor_id(self.novaclient, 'gluon-flavor')
        if self.flavor_id == '':
            self.flavor_id = osutils.create_flavor(self.novaclient,
                                                   'gluon-flavor',
                                                   512, 1, 1)
            if self.flavor_id is None:
                raise Exception('Nova flavor creation failed')

    def _cleanup_flavor(self):
        logger.info('Deleting flavor')
        self.novaclient.flavors.delete(self.flavor_id)

    def _wait_for_instance(self, instance):
        if not self._wait_for_instance_status_change(self.novaclient,
                                                     instance):
            vm_status = osutils.get_instance_status(self.novaclient, instance)
            logger.error("Instance '%s' cannot be booted. Status is '%s'"
                         % (instance, vm_status))
            return None
        else:
            logger.info("Instance '%s' is ACTIVE." % instance)

    def _wait_for_instance_status_change(self, nova, vm):
        sleep_time = 3
        count = self.vm_boot_timeout / sleep_time
        while True:
            status = osutils.get_instance_status(nova, vm)
            logger.debug("Status: %s" % status)
            if status == "ACTIVE":
                return True
            if status == "ERROR" or status == "error":
                return False
            if count == 0:
                logger.debug("Booting a VM timed out...")
                return False
            count -= 1
            time.sleep(sleep_time)

    def _build_user_data(self, instance_ip, gw_ip, test_ip):
        return ("#!/bin/sh\n\n"
                "killall -9 udhcpc\n"
                "ifconfig eth0 %s netmask 255.255.255.0\n"
                "route add default gw %s\n"
                "while true; do\n"
                " ping -c 1 %s 2>&1 >/dev/null\n"
                " RES=$?\n"
                " if [ \"Z$RES\" = \"Z0\" ] ; then\n"
                "  echo 'vPing OK'\n"
                "  break\n"
                " else\n"
                "  echo 'vPing KO'\n"
                " fi\n"
                " sleep 1\n"
                "done\n" % (instance_ip, gw_ip, test_ip))

    def _boot_vms(self):
        neutron_ports = self.neutronclient.list_ports()
        neutron_port_ids = [p['id'] for p in neutron_ports['ports']]
        logger.info("Neutron port IDs: %s" % neutron_port_ids)

        for port_id in self.port_ids:
            if port_id not in neutron_port_ids:
                raise Exception('Gluon port %s not found among existing '
                                'Neutron ports' % port_id)

        ip_instance_1 = '10.10.0.2'
        gw_instance_1 = '10.10.0.1'

        ip_instance_2 = '10.10.1.2'
        gw_instance_2 = '10.10.1.1'

        logger.info('Booting first instance.')
        user_data_1 = self._build_user_data(ip_instance_1,
                                            gw_instance_1,
                                            ip_instance_2)
        self.instance_1 = \
            self.novaclient.servers.create(name='Gluon VM 1',
                                           flavor=self.flavor_id,
                                           image=self.image_id,
                                           nics=
                                           [{"port-id": self.port_ids[0]}],
                                           config_drive=True,
                                           userdata=user_data_1)
        self._wait_for_instance(self.instance_1)

        logger.info('Booting second instance.')
        user_data_2 = self._build_user_data(ip_instance_2,
                                            gw_instance_2,
                                            ip_instance_1)
        self.instance_2 = \
            self.novaclient.servers.create(name='Gluon VM 2',
                                           flavor=self.flavor_id,
                                           image=self.image_id,
                                           nics=
                                           [{"port-id": self.port_ids[1]}],
                                           config_drive=True,
                                           userdata=user_data_2)
        self._wait_for_instance(self.instance_2)

        error_code = self._check_ping(self.instance_1, ip_instance_2, 200)
        if error_code != 0:
            raise Exception('Ping of instance 1 to %s failed' % ip_instance_2)

        error_code = self._check_ping(self.instance_2, ip_instance_1, 200)
        if error_code != 0:
            raise Exception('Ping of instance 2 to %s failed' % ip_instance_1)

    def _check_ping(self, instance, test_ip, timeout):
        logger.info("Waiting for ping...")
        EXIT_CODE = -1
        sec = 0
        tries = 0

        while True:
            time.sleep(1)
            p_console = instance.get_console_output()
            if "vPing OK" in p_console:
                logger.info("vPing detected!")
                EXIT_CODE = 0
                break
            elif "failed to read iid from metadata" in p_console or tries > 5:
                EXIT_CODE = -2
                break
            elif sec == timeout:
                logger.info("Timeout reached.")
                break
            elif sec % 10 == 0:
                if "request failed" in p_console:
                    logger.debug("It seems userdata is not supported "
                                 "in nova boot. Waiting a bit...")
                    tries += 1
                else:
                    logger.debug("Pinging %s. Waiting for response..."
                                 % test_ip)
            sec += 1

        return EXIT_CODE

    def _cleanup_instances(self):
        logger.info('Deleting instances.')
        self.novaclient.servers.delete(self.instance_1.id)
        self.novaclient.servers.delete(self.instance_2.id)


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
