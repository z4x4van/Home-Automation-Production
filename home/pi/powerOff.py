import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(int(sys.argv[1]),GPIO.OUT)
GPIO.cleanup()
