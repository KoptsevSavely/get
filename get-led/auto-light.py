import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
state = 0
photo = 6
GPIO.setup(photo, GPIO.IN)
while True:
    a = GPIO.input(photo)
    GPIO.output(led, (not(a)))
    