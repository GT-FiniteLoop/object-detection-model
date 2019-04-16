# Object Detection Model:

### System Requirements
```
Install instructions are for Linux and tested specifically on Ubuntu 16.04
```

### Install Instructions
```
Run the following commands to install git, clone our repository, and run our installation script

$sudo apt-get install git
$git clone https://github.com/GT-FiniteLoop/object-dectection-model.git

$cd object-detction-model
$chmod +x ./tf_install.sh

$sudo ./tf_install.sh
```

### Run Instructions
```
The two implemented modes are live and local.
Live will take the first available camera and local will take a provided video file.

python3 model.py  --mode live
or
python3 model.py --mode local --video <video file>
```
