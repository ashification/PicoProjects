from picozero import pico_led
from picozero import LED
import utime

#Declare GPIO usage
blue_led = LED(21)

while True:

    #Blink Board LED and blue LED to show pwr and tx
    pico_led.blink() #Pico board LED
    blue_led.blink()
    utime.sleep(5)
