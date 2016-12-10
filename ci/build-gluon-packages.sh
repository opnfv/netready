#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

echo "Running make to build Gluon packages..."

pushd ../build
make
popd

echo "make finished"
