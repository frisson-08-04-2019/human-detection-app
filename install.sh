#!/bin/bash

conda create -n human-detection-app pip python=3.6 -y
source activate human-detection-app
git submodule init
git submodule update
pip install -r requirements.txt
pip install -r human_detection_engine/requirements.txt
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000
