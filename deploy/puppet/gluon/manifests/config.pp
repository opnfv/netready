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
