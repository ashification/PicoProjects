from picozero import Pot # Pot is short for Potentiometer
import utime

blue_varistor = Pot(28) # Connected to pin A1 (GP_27)
red_varistor = Pot(27) # Connected to pin A1 (GP_27)
white_varistor = Pot(26) # Connected to pin A1 (GP_27)

while True:
   utime.sleep(1)
   # Read potentiometer sensor data         
   blue_varistor_value = int(100 - (blue_varistor.value*100))
   red_varistor_value = int(100 - (red_varistor.value*100))
   white_varistor_value = int(100 - (white_varistor.value*100))

   json_data = {
                    "BluePotValue": blue_varistor_value,
                    "RedPotValue": red_varistor_value,
                    "WhitePotValue": white_varistor_value,
                }
   print(json_data)
