# Code Source from https://www.instructables.com/DHT11-With-Raspberry-Pi-Pico/
# Slight modifications to the code given in the link taken from thread here https://forums.raspberrypi.com/viewtopic.php?t=343485
# Works with current version of MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350


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


