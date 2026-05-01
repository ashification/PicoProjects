# PicoProjects

This repository serves as examples for code to be used in Raspberry Pi Pico projects.
## Hardware
If you do not have access to any of the hardware please refer to the section below regarding the Wokwi simulator
<br/>

### Equipment list
There are a number of items you will need to complete these exercises.
* 1x Breadboard
    * Also referred to a protoboards, devboards etc these are boards that require no [soldering](https://en.wikipedia.org/wiki/Soldering#:~:text=Soldering%20(US%3A%20%2F%CB%88s,a%20strong%20and%20durable%20joint) and allow for quick and easy building of circuits (kinda like an electronic lego base plate)
* 1x Raspbery pi pico
    * More details on this micorcontroller below
* 1x LED
    * [LED](https://en.wikipedia.org/wiki/Light-emitting_diode) stands for Light Emitting Diode. These are small handy lights that always add a bit of pizaz to any electronics project. You will need 1 but can get creative with examples showing the use of up to 4 differnet colours
* 1x 220Ω resistor
    * A [resistor](https://en.wikipedia.org/wiki/Resistor#:~:text=A%20resistor%20is%20a%20passive,transmission%20lines%2C%20among%20other%20uses.) restricts the flow of current and helps us to control how much goes to a component/circuit
* 1x Potentiometer
    * A [Potentiometer](https://en.wikipedia.org/wiki/Potentiometer) is a form of variable resistor that you can control the value of by turning it up or down (like the volume on a speaker)
<br/>

![Fritzing Images of Hardware](https://github.com/ashification/PicoProjects/blob/main/Equipment%20list%20fritzing%20image.png)
<br/><br/>

### Raspberry Pi Pico Microcontroller
The Raspberry Pi Pico is a micro controller produced by Raspberry Pi. <br/>
You can read more specific details about the device  here: [RPI Pico Series Official Documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) <br/>
For versioning and compatability please note this was all developed on and for MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350 unless otherwise stated<br/><br/>
Below is the Pin Out Diagram for the model used<br/>
![Pin Out](https://github.com/ashification/PicoProjects/blob/main/pico-2-pinout.jpg) 
<br/><br/>



## Wokwi Simulator 
If you do not have access to a Pico, the components or have the ability to install and run the MicropythonIDE listed you can use Wokwi.com.
Wokwi will allow us to simulate the hardware aspect of this course. Like with all projects remember to save your code regularly!!!
There will be examples for Wokwi in each of the mini projects but to get started you can go to the link here [Base Pico Project ](https://wokwi.com/projects/462827756040158209) for the base project and create a copy for yourself.
<br/><br/>

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
