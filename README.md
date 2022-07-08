# InstallOpenCVRaspberryPi

This is a simple project I'm putting together for tracking animals in their natural environment. Here I to installed [OpenCV](https://opencv.org/) on the [Raspberry Pi 4 B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) with the standard [Raspberry Pi camera](https://www.raspberrypi.com/products/camera-module-v2/) connected to capture objects in motion.  

## Part 1: Install OpenCV

Briefly, the shell script InstallOpenCVRaspberryPi.sh can be used to install OpenCV using a python virtual environment. To execute the installation script and to have the virtual environment activated into the shell being used simply use ``` . InstallOpenCVRaspberryPi.sh ``` in lieu of ``` ./InstallOpenCVRaspberryPi.sh ``` 

Once running the user of the installation script will be prompted to name the project folder and the script will place the virtual environment into this newly created folder.

Once OpenCV is installed the user can type ``` python3 ``` into the terminal and can check the installation worked by importing open cv2, i.e, ``` import cv2 ``` . If no errors arise the installation has worked.

## Part 2: Run motion detection script 

**Note:** This next section assumes you have the Raspberry Pi camera or another camera attached to the pi to capture images - otherwise this will not work. Additionally, the python script will only acquire images when motion is detected and additional configuration may be required to get the camera communicating with the pi and is not covered here.

The python file, motionDetectionCapture.py, is a simple motion detection script which can be run from the terminal. The file, motionDetectionCapture.py, should be placed in the virtual environment folder named env and can be run using python3 from the activated virtual environment. Images acquired can be found in the folder ``` savedImages ``` and can be 
deleted all at once by running the shell script ``` ./deleteJPGs.sh ``` .

Enjoy!

Credit given to the following links for providing guidance on how to create these scripts and for providing information on dependencies needed to install OpenCV. 

1. [Single Board Blog By:  Can Berk Durmus ](https://singleboardblog.com/install-python-opencv-on-raspberry-pi/)
2. [Motion Detection](https://www.youtube.com/watch?v=MkcUgPhOlP8)
