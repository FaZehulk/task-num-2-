# sender
from microbit import *
from ultrasonic import Ultrasonic
import radio
radio.config(group=10)
radio.on()

ultrasonic_sensor = Ultrasonic()
while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    movment= pin2.read_digital()

    if movment == 1:
        radio.send =='help or else !!!!!'
   
        
        

