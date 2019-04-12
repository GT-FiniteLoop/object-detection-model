# !/bin/bash
# 64-bit Ubuntu version 16.04.6
# TensorFlow version 1.9
#
# NOTE TO SELF: Installation instructions should include chmod for script and install for git
# NOTE TO SELF: Installation instructions should include instructions on how to run the model

cd ~
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip
sudo apt-get install git
pip3 install --ignore-installed --upgrade tensorflow==1.9
pip3 install pillow==5.4.1 lxml==4.3.1 jupyter==1.0.0 matplotlib==3.0.2 opencv-python

cd ~
sudo mkdir ~/TensorFlow
cd ~/TensorFlow
git clone https://github.com/tensorflow/models.git
cd models/research
sudo wget https://github.com/protocolbuffers/protobuf/releases/download/v3.7.1/protoc-3.7.1-linux-x86_64.zip
sudo unzip protoc-3.7.1-linux-x86_64.zip
export PYTHONPATH=$PYTHONPATH:/TensorFlow/models/research/object_detection
export PYTHONPATH=$PYTHONPATH:/TensorFlow/models/research:/TensorFlow/models/research/slim
source ~/.bashrc
./bin/protoc object_detection/protos/*.proto --python_out=.

cd ~/TensorFlow/models/research/
sudo python3 setup.py build
sudo python3 setup.py install
