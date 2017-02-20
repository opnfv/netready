#
# Copyright (c) 2017 Ericsson and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
class gluon::install {

  package { 'python-click':
    ensure   => installed,
  }

  package { 'gluon':
    ensure   => installed,
  }

}
