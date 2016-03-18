Connect an Arduino bluetooth module to a desktop using a three way handshake protocol.

Master and slave, respectively the desktop and the arduino, applications are implemented. 

> The desktop application is located in the root of this project and is called: arduino.py

> The Arduino application is located at: bluetoothStandalone/bluetoothStandalone.ino

Other files are explained at the end of this file.


Needed:

> Ubuntu

> Arduino Uno

> HC-05 Bluetooth module

> libbluez-dev

> pybluez

The default key for the modules is: 1234.

The password can be set using: bluetooth-agent 1234 &



The folder bluetoothMinimum is the the minimal testing setup for configuring and testing the bluetooth module.

The folder bluetoothStandaloneLCD is the same as the bluetoothStandalone application, except that it adds LCD functionality.

The folder bluetoothSoftwareSerial is an attempt to get the HC-05 bluetooth module working using not only the hardware serial port, but also the software serial ports using digital pinouts.

The main.py is used to run a simulation of the Arduino modules, but is still under construction.

