from umqtt.simple import MQTTClient
from picozero import pico_led
from picozero import LED
from picozero import Speaker
from picozero import Button
from picozero import Switch
from picozero import Pot # Pot is short for Potentiometer
from machine import Pin, I2C
from math import trunc
import network
import config
import time 
import network
import utime
import sys
import ujson
#import BME280
#import mip




#Declare GPIO usage
red_button = Button(14)
green_button = Button(15)
#dev_board_speaker = Speaker(18)
#dev_board_led = LED(20)
blue_led = LED(21)
red_led = LED(20)
yellow_led = LED(19)
green_led = LED(18)
#dev_board_button = Button(19)
blue_varistor = Pot(28) # Connected to pin A1 (GP_27)
red_varistor = Pot(27) # Connected to pin A1 (GP_27)
white_varistor = Pot(26) # Connected to pin A1 (GP_27)
#ldr = machine.ADC(26) # Connected to pin A0 (GP_26)

last_blue_varistor_value = 0
last_red_varistor_value = 0
last_white_varistor_value = 0
loop_count = 0

# Constants for MQTT Topics
#MQTT_TOPIC_TEST = config.mqtt_pub_topic
#MQTT_TOPIC_LED = config.mqtt_sub_topic

MQTT_TOPIC_TEST = 'picow'
MQTT_TOPIC_RedPot = 'picow/redpot'
MQTT_TOPIC_BluePot = 'picow/bluepot'
MQTT_TOPIC_WhitePot = 'picow/whitepot'
MQTT_TOPIC_LED = 'picow/led'

# MQTT Parameters
MQTT_SERVER = config.mqtt_server
MQTT_PORT = 1883 #config.mqtt_port
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
                            #user=MQTT_USER,
                            #password=MQTT_PASSWORD,
                            #keepalive=MQTT_KEEPALIVE,
                            #ssl=MQTT_SSL,
                            #ssl_params=MQTT_SSL_PARAMS
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
    if message == b'RED ON':
        #print('Turning LED ON')
        red_led.on()  # Turn LED ON
    elif message == b'RED OFF':
        #print('Turning LED OFF')
        red_led.off()  # Turn LED OFF
    elif message == b'YELLOW ON':
        #print('Turning LED OFF')
        yellow_led.on()  # Turn LED OFF
    elif message == b'YELLOW OFF':
        #print('Turning LED OFF')
        yellow_led.off()  # Turn LED OFF
    elif message == b'GREEN ON':
        #print('Turning LED OFF')
        green_led.on()  # Turn LED OFF
    elif message == b'GREEN OFF':
        #print('Turning LED OFF')
        green_led.off()  # Turn LED OFF
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
            
            pico_led.blink() #Pico board LED
            blue_led.blink()
            
            if red_button.is_pressed == True:
               print('red button pressed', red_button.is_pressed)
               publish_mqtt(MQTT_TOPIC_LED, str("RED ON"))
               client.check_msg()
               
            if green_button.is_pressed == True:
               print('red button pressed', green_button.is_pressed)
               publish_mqtt(MQTT_TOPIC_LED, str("RED OFF"))
               client.check_msg()
               
            #print('Passed buttons')
           
        # Read sensor data         
            blue_varistor_value = int(100 - (blue_varistor.value*100))
            red_varistor_value = int(100 - (red_varistor.value*100))
            white_varistor_value = int(100 - (white_varistor.value*100))
            #print('Passed pots')
            


            if blue_varistor_value != last_blue_varistor_value or red_varistor_value != last_red_varistor_value or white_varistor_value != last_white_varistor_value:
                last_blue_varistor_value = blue_varistor_value
                last_red_varistor_value = red_varistor_value
                last_white_varistor_value = white_varistor_value
                #print('blue var rounded', blue_varistor_value)

                #Create JSON Message
                json_data = {
                        "BluePotValue": blue_varistor_value,
                        "RedPotValue": red_varistor_value,
                        "WhitePotValue": white_varistor_value,
                        }
                
                # Publish as MQTT payload
                #publish_mqtt(MQTT_TOPIC_BluePot, str(blue_varistor_value))
                #publish_mqtt(MQTT_TOPIC_RedPot, str(red_varistor_value))
                #publish_mqtt(MQTT_TOPIC_WhitePot, str(white_varistor_value))
                publish_mqtt(MQTT_TOPIC_TEST, ujson.dumps(json_data))
                #print('Passed pub')
                
                
            #print('Passed json')

            # Delay 1 seconds
            #time.sleep(5)
            

except Exception as e:
    print('Error:', e)

    
   
