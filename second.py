#Pogram to turn led bulb on & off on user`s input

import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    i = int(input(""))
    if i==1:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("ON")
    elif i==0:
        GPIO.output(LED_PIN, GPIO.LOW)
        print("OFF")
    else:
        GPIO.cleanup()
