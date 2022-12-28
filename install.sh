#!/usr/bin/env bash

set -o pipefail

if [[ $(id -u) -ne 0 ]] ; then echo "Please run as superuser." ; exit 1 ; fi

echo "Update repository..."
apt-get update -y


echo "Install Python..."
apt-get -y install python3 python3-pip python3-venv python3-dev


echo "Create Python virtual environment..."
sudo -u $SUDO_USER python3 -m venv env


source env/bin/activate


echo "Install python packages..."
python3 -m pip install --default-timeout=100 -r requirements.txt


deactivate


echo "Installation completed."
