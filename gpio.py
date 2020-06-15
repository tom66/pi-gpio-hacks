import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  

GPIO.setup(12, GPIO.OUT)  

while True:
    GPIO.output(12, 1)
    GPIO.output(12, 0)
