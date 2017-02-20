#
# Copyright (c) 2017 Ericsson and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
class gluon::config {

  file { '/etc/proton/proton-shim.conf':
    ensure  => 'file',
    owner   => 'proton',
    group   => 'proton',
    mode    => '640',
    content => template('gluon/proton-shim.conf.erb'),
  }

  file { '/etc/proton/proton.conf':
    ensure  => 'file',
    owner   => 'proton',
    group   => 'proton',
    mode    => '640',
    content => template('gluon/proton.conf.erb'),
  }

}
