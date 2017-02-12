class gluon inherits ::gluon::params {

  $bind_ip          = $::gluon::params::bind_ip
  $port             = $::gluon::params::port

  $odl_bind_ip      = hiera(opendaylight::odl_bind_ip, $::gluon::params::odl_bind_ip)
  $odl_rest_port    = hiera(opendaylight::odl_rest_port, $::gluon::params::odl_rest_port)
  $odl_username     = hiera(opendaylight::username, $::gluon::params::odl_username)
  $odl_password     = hiera(opendaylight::password, $::gluon::params::odl_password)

  $etcd_bind_ip     = hiera(tripleo::profile::base::etcd::bind_ip, $::gluon::params::etcd_bind_ip)
  $etcd_client_port = hiera(tripleo::profile::base::etcd::client_port, $::gluon::params::etcd_client_port)

  class { '::gluon::install': } ->
  class { '::gluon::config': } ~>
  class { '::gluon::service': } ->
  Class['::gluon']

}
