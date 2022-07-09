#!/bin/sh
#update os
sudo apt-get update && sudo apt-get upgrade
#clear terminal
clear
#ask user what the foldername should be for the project
echo PLEASE PROVIDE NAME FOR PROJECT FOLDER:
#capture user input
read folderName
#create folder for project 
mkdir $folderName
cd $folderName
#create and activate virtual environment
python3 -m venv env
source env/bin/activate
#upgrade pip if needed
pip install --upgrade pip setuptools wheel
#upgrade numpy
pip install numpy --upgrade
#install dependencies needed for opencv
sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev
#install opencv
pip install opencv-contrib-python==4.5.3.56
#remove unused packages
sudo apt autoremove
#moves python files into env folder
cd ..
mv deleteJPGs.sh motionDetectionCapture.py $folderName
#create directory to store images
cd $folderName
