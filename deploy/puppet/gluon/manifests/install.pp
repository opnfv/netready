class gluon::install {

  package { 'python-click':
    ensure   => installed,
  }

  package { 'gluon':
    ensure   => installed,
  }

}
