from umqtt.simple import MQTTClient
from picozero import pico_led
from picozero import LED
from picozero import Button
import network
import config
import time 
import network
import utime
import sys

#Declare GPIO usage
#Buttons
red_button = Button(14)
green_button = Button(15)

#LEDs 
blue_led = LED(21)
red_led = LED(20)

# Constants for MQTT Topics
MQTT_TOPIC_TEST = 'picow'
MQTT_TOPIC_LED = 'picow/led'

# MQTT Parameters
MQTT_SERVER = config.mqtt_server
MQTT_PORT = config.mqtt_port
MQTT_USER = config.mqtt_username
MQTT_PASSWORD = config.mqtt_password
MQTT_CLIENT_ID = b"raspberrypi_picow"
MQTT_KEEPALIVE = 7200
MQTT_SSL = False   # set to False if using local Mosquitto MQTT broker
MQTT_SSL_PARAMS = {'server_hostname': MQTT_SERVER}


def initialize_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Connect to the network
    wlan.connect(ssid, password)

    # Wait for Wi-Fi connection
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Waiting for Wi-Fi connection...')
        time.sleep(1)

    # Check if connection is successful
    if wlan.status() != 3:
        return False
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True

def connect_mqtt():
    try:
        client = MQTTClient(client_id=MQTT_CLIENT_ID,
                            server=MQTT_SERVER,
                            port=MQTT_PORT,
                            )
        client.connect()
        return client
    except Exception as e:
        print('Error connecting to MQTT:', e)
        raise  # Re-raise the exception to see the full traceback

def publish_mqtt(topic, value):
    client.publish(topic, value)
    print(topic)
    print(value)
    print("Publish Done")

# Subcribe to MQTT topics
def subscribe(client, topic):
    client.subscribe(topic)
    print('Subscribe to topic:', topic)
    
# Callback function that runs when you receive a message on subscribed topic
def my_callback(topic, message):
    # Perform desired actions based on the subscribed topic and response
    print('Received message on topic:', topic)
    print('Response:', message)  
        
    # Check the content of the received message
    if message == b'RED ON' :
        #print('Turning LED ON')
        red_led.on()  # Turn LED ON
    elif message == b'RED OFF' :
        #print('Turning LED OFF')
        red_led.off()  # Turn LED OFF
    else:
        print('Unknown command')

try:
    if not initialize_wifi(config.wifi_ssid, config.wifi_password):
        print('Error connecting to the network... exiting program')
    else:
        # Connect to MQTT broker, start MQTT client
        client = connect_mqtt()
        client.set_callback(my_callback)
        subscribe(client, MQTT_TOPIC_LED)
        while True:
            
            #Blink LEDs to show pwr and tx
            pico_led.blink() #Pico board LED
            blue_led.blink()
            
            #Read in Button press data
            if red_button.is_pressed == True:
               print('red button pressed', red_button.is_pressed)
               publish_mqtt(MQTT_TOPIC_LED, str("RED ON"))
               client.check_msg()
               
            if green_button.is_pressed == True:
               print('green button pressed', green_button.is_pressed)
               publish_mqtt(MQTT_TOPIC_LED, str("RED OFF"))
               client.check_msg()
               

            # Delay 1 seconds
            time.sleep(1)
            

except Exception as e:
    print('Error:', e)

