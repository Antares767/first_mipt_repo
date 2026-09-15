import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
num = 0
sleep_time = 0.2

def dec2bin(value):
    return [int(element) for element in bin(value)[2::].zfill(8)]

while True:

    if (GPIO.input(up) == 1) and (GPIO.input(down) == 1):
        num = 8
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    elif GPIO.input(up):
        num += 1

        if num > 8:
            num = num % 8
        if num <= 0:
            num = 8 + num
            
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    elif GPIO.input(down):
        num -= 1
        if num > 8:
            num = num % 8
        if num <= 0:
            num = 8 + num
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    
    GPIO.output(leds, dec2bin(num))