# PicoProjects

This repository serves as examples for code to be used in Raspberry Pi Pico projects.
For versioning and compatability please note this was all developed on and for MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350 unless otherwise stated

## The mini projects are:
- Example 1 - Blink an LED
- Example 2 - Control an LED with a button
- Example 3 - Using a potentiometer
- Example 4 - Using a HC-SR04 Range finder 
- Example 5 - DHT11 humidity and temperature measurement
- Example 6 - Connecting to Wi-Fi and webscraping
- Example 7 - Connecting to an MQTT Broker to send messages
- Example 8 - Combines all previous examples into 1 program

## The Major Project - The Demo Box
The Demo box code is my personal development for testing out new features to add to the above examples list and demonstrating new features.


## Integrations
I am integrating the above code with a Mosquitto MQTT broker and a web based dashboard using NodeRed all hosted on my Raspberry Pi 5.<br/><br/> 

### Installers
The code for setting up both can be found in my [raspberry pi base installers script](https://github.com/ashification/RPISetup/blob/main/Installers/rpi_base_installer.sh) under the followng headings:
- "# Install Mosquitto MQTT Broker"
- "## Installing nodeRed"
<br/>

### Dashboard
If youre looking for help/examples for building your workflows/configuring your NodeRed dashboards <br/>
you can jump over to [raspberry pi base installers script](https://github.com/ashification/NodeRedProjects) for a few examples
