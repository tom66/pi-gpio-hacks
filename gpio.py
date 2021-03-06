import time
import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM)  

GPIO.setup(12, GPIO.OUT)  
GPIO.setup(13, GPIO.IN)  

def cb(*args):
    GPIO.output(12, 1)
    GPIO.output(12, 0)

GPIO.add_event_detect(13, GPIO.RISING, callback=cb)  

while True: 
    time.sleep(0.001)