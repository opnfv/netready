class gluon::post inherits gluon {

  file { '/etc/proton/proton-shim.conf':
    ensure  => 'file',
    owner   => 'proton',
    group   => 'proton',
    mode    => 'go+w',
    content => template('gluon/proton-shim.conf.erb'),
  }

}
