# Task 7 - MQTT Connectivity  <br/><br/> 
## Hardware
For this task you will need 2 LEDs and 2 Butttons from your pack along with the breadboard and pico.
![Parts Requires](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/task7_mqttequipment.png)
<br/> <br/> 

You can either start fresh or take your previous circuit and continue to add to the board like so:
![Diagram for breadboard assembly](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/task7_mqttcct.png)
<br/><br/> 

## Wokwi
For Wokwi you will need to build your board and add your components. For each section the full soloution will be provided (python code and JSON for diagram) both in the repository here as well as a working wokwi project.
Do try it yourself first and go to the examples as references if you get stuck  
- [Task 7 JSON code for Wokwi Diagram ](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/wokwi_task7_diagram.json)
- [Task 7 Wokwi Full Soloution](https://wokwi.com/projects/463196588054589441)

## MQTT Broker
Depending on what equipment you have available to you you might be utiliising an MQTT broker that is hosted locally on another raspberry pi (scripts needed to install a Mosquitto MQTT broker on Raspberry Pi can be found [here](https://github.com/ashification/RPISetup/blob/main/Installers/rpi_base_installer.sh)).
Once installed you can get the IP details of your broker:
1. Open a terminal session on the raspberry pi hosting your broker
2. Run ifconfig
3. Look for the words "*inet addr*"
  - e.g.  inet addr: 192.168.XX.XXX 
<br/> 

If you do not have access to one you can utilise the HiveMQ Free Broker by going to their [dashboard](https://www.mqtt-dashboard.com/) as seen below:
<br/>
![Screenshot for hiveMq Dashboard](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/hivemq-dashboard.png)
<br/><br/> 

When you click on connect button, a pop up will appear. In it the details shown are what you will use in your MQTT client. In our case we will need the 2 parameters circled to add to our config file
![Screenshot for hiveMQ Broker Details](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/hivemq-brokerdetails.png)
<br/><br/> 

Once youve added the details to your pico project (physical hardware or Woki simulator) you can watch your messages coming in and out of the broker via your terminal.
If you are using the HiveMQ broker you can do this via the [HiveMQ Websocket Client](https://www.hivemq.com/demos/websocket-client/). Seen below you can 
1. Edit the connection details, e.g. add in credtentials if you want to secure your messages
- ![Screenshot for Websocket Client](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/hiveMQ-websocketclient_connect.png)
2. Subscribe to your topics
- ![Screenshot for Websocket Client](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/hiveMQ-websocketclient_pretestmessage.png)
3. And publish messages
- ![Screenshot for Websocket Client](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/hiveMQ-websocketclient_testmessage.png)
<br/>

Once your system is up and running youll be able to see your messages appear in your broker (see below example for HiveMQ) and in your terminal (both on the physical pico, raspberry pi, and Wokwi terminal)
![Screenshot for Websocket Client](https://github.com/ashification/PicoProjects/blob/main/Task_7-MQTT_Connectivity/hiveMQ-websocketclient.png)


<br/><br/> 
