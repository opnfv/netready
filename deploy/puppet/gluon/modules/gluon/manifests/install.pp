class gluon::install inherits gluon {

  package { 'python-click':
    ensure => installed,
  }

  package { 'gluon':
    ensure  => installed,
  }

}
