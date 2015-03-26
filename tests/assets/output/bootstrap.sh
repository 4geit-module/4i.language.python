#!/bin/bash

# xyz
# Copyright (C) 2014  xyz developers  (see AUTHORS)
#
# All rights reserved.

pushd /tmp/.4geit/module/4i.language.python_master/tests/assets/build/

virtualenv2 .
source bin/activate

pip install --upgrade pip
pip install --allow-all-external -r requirements.txt
./build.sh

deactivate

popd
