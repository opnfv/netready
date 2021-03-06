#!/bin/bash
#
# Copyright (c) 2017 Ericsson and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
set -o errexit
set -o nounset
set -o pipefail

echo "Running make to build Gluon packages..."

pushd ../build
make
popd

echo "make finished"
