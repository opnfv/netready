class gluon::service {

  service { 'openstack-proton-server':
    ensure   => running,
    enable   => true,
  }

  service { 'openstack-proton-shim-server':
    ensure   => running,
    enable   => true,
  }

}
