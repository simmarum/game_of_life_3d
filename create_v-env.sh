#!/bin/bash

# Simple bash script to recreate env for this repository
# Activate env by typing
#
# source ./v-env/bin/activate
#

set -e
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

rm -rf $SCRIPTPATH/v-env

python3 -m venv $SCRIPTPATH/v-env
. $SCRIPTPATH/v-env/bin/activate

pip3 install --compile \
autopep8==1.4.4 \
numpy==1.18.1 \
pycodestyle==2.5.0 \
pygame==1.9.6 \
PyOpenGL==3.1.4 \
PyOpenGL-accelerate==3.1.4