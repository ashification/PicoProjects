# Code Source from https://www.instructables.com/DHT11-With-Raspberry-Pi-Pico/
# Slight modifications to the code given in the link taken from thread here https://forums.raspberrypi.com/viewtopic.php?t=343485
# Works with current version of pico (RPI2040) and micropython (raspberry Pi Pico) installed 2025-09-25

import dht 
import machine 
import utime 
pin = machine.Pin(16) 
data_dht = dht.DHT11(pin) 
while True: 
utime.sleep(2) 
data_dht.measure() 
print() 
print ( f" temperature (C) :{data_dht.temperature()}") 
print ( f" humidity (%): {data_dht.humidity()} ")

