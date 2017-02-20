#
# Copyright (c) 2017 Ericsson and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
class gluon::params {

  $bind_ip          = '127.0.0.1'
  $port             = '2705'
  $odl_bind_ip      = '0.0.0.0'
  $odl_rest_port    = '8181'
  $odl_username     = 'admin'
  $odl_password     = 'admin'
  $etcd_bind_ip     = '127.0.0.1'
  $etcd_client_port = '2379'

}
