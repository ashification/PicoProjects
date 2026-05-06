# Task 6 - Temperature and Humidity  <br/><br/> 
## Hardware
For this task you will only need the breadboard and pico from your pack. You can either start fresh or build on your previous board:
![Parts Requires](https://github.com/ashification/PicoProjects/blob/main/Task_6-WiFi_Connectivity/task6wifiequipment.png)
<br/> <br/> 



## Wokwi
For Wokwi you will need to build your board and add your components. For each section the full soloution will be provided (python code and JSON for diagram) both in the repository here as well as a working wokwi project.

<br/>

  ### Pico board 
  Make sure your pico board is configured to be a Pico-W (wireless) like the below in your JSON file (type and attributes are important here) otherwise you wont be able to use any internet features
  ```
   {
      "type": "board-pi-pico-w",
      "id": "pico",
      "top": -137.55,
      "left": -82.8,
      "attrs": { "env": "micropython-20241129-v1.24.1" }
  }
  ```
  <br/>
  
  ### Wokwi internet details
  When setting up the details for the internet access in your config file use the below for Wokwi
  * wifi_ssid = "Wokwi-GUEST"
  * wifi_password = ""

  ### Wokwi sample soloution
  Do try it yourself first and go to the examples as references if you get stuck:  
  - [Task 6 JSON code for Wokwi Diagram ](https://github.com/ashification/PicoProjects/blob/main/Task_6-WiFi_Connectivity/wokwi_task6_diagram.json)
  - [Task 6 Wokwi Full Soloution](https://wokwi.com/projects/463209388104992769)
<br/><br/> 
