import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  

GPIO.setup(12, GPIO.OUT)  

state = 0

while True:
    GPIO.output(12, state)
    state = 1 - state
