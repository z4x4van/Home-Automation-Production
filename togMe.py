import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(sys.argv[1]),GPIO.OUT)
GPIO.output(int(sys.argv[1]),GPIO.HIGH)

SleepTimeL = 1

GPIO.output(int(sys.argv[1]),GPIO.LOW)
time.sleep(SleepTimeL)
GPIO.cleanup()
