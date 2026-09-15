import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
photo = 6
GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo, GPIO.IN)
# state = 0
# period = 0.2

while True:
    GPIO.output(led, not GPIO.input(photo))
