#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)


for x in range(11):
	GPIO.output(26, True)
	print(x)
	time.sleep(0.5)
	GPIO.output(26, False)
	time.sleep(0.5)

GPIO.cleanup()
