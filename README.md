# labday2017-2-hexapod-first-steps

## First steps toward making a hexapod autonomous

This will be an attempt at getting a program running on an Intel Euclid development kit to send commands to a PhantomX Hexapod.  The ultimate goal will be to have a program manage the sensors on the Euclid device (depth camera, motion camera, accelerometer, gyroscope, etc...) via interacting with them through ROS, being able to interpret the information, and then being able to direct the robot's actions.  The first step toward taking first steps starts with being able to send serial commands from a program running on the Eudlic device to the hexapod.  In order to do so, some setup is needed prior to programming.  Many of these steps will be taken prior to labday.

### On the Euclid device, setup entails:

* logging into the device via VNC
* setting up an ssh server
* logging into the device via ssh
* loading sbt, Scala, Akka
* possibly loading rosjava

### On the hexapod, setup entails:

* modification of Arduino sketch running on the Arbotix-M board
* some reconfiguration of jumpers

A USB-to-serial cable will connect the Euclid device to the PhantomX.  A simple program written in Scala and/or Akka will be written that sends commands to the hexapod.  Code from the Virtual Commander will be referenced as a guide.  The success case will be getting the hexapod to respond to those commands.  If this happens earlier in the day, then the next step will be to try to incorporate information from the time-of-flight camera for obstacle detection.

## Risks

* The required hardware (a USB to serial cable) may not be quite right.  If this turns out to be the case, the time will be spent getting the program to interact with the onboard sensors via ROS.

## Ideas for future work

* using SLAM to map out a room
* sentry to recognize humans
* recognizing and responding to hand gestures
* recognizing and responding to voice commands
* learning how to walk from scratch using a genetic algorithm to evolve gaits, given servo feedback, accelerometer input, etc..
* evolving the most efficient running gait
* learning how to climb stairs
* playing fetch

## Reference material
* Intel Euclid  https://click.intel.com/intelr-euclidtm-development-kit.html
* PhantomX Hexapod http://www.trossenrobotics.com/phantomx-ax-hexapod.aspx

## Team
* Bruce Ferguson
* Bart Van Deenen
* Quirijn Meulenberg
* Hakim Khalafi

# Various Notes
ssh -o PreferredAuthentications=password euclid@172.20.10.9 -L 8100:localhost:80
http://172.20.10.9:8080/stream?topic=/camera/color/image_raw
