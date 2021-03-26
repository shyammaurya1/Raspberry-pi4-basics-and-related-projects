#program to light bulb(led)

import RPi.GPIO as GPIO
import time

LED_PIN = 17 #check GPIO pin no.

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT) #output

while True:
    GPIO.output(LED_PIN, GPIO.HIGH) #HIGH : ON
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW) #LOW :OFF
    time.sleep(1)

GPIO.cleanup()
