from picozero import pico_led
from picozero import LED
from picozero import Speaker
from picozero import Button
import utime

#Declare GPIO usage
red_button = Button(14)
green_button = Button(15)
dev_board_speaker = Speaker(11)
blue_led = LED(21)

while True:

    #Blink Board LED to show pwr and tx
    pico_led.blink() #Pico board LED
    
    #Read in Button press data
    if red_button.is_pressed == True:
       print('red button pressed', red_button.is_pressed)
       blue_led.off()
       
       
    if green_button.is_pressed == True:
       print('green button pressed', green_button.is_pressed)
       blue_led.on()
       dev_board_speaker.play() # play the middle c for 0.1 seconds
