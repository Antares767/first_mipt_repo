import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac_bits, GPIO.OUT)
dynamic_range = 3.3

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
       
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def set_number(self, number):
        number = max(0, min(int(number), 255))
        states = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, states)

        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {states}\n")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.set_number(0)
            return 

        number = int(voltage / dynamic_range * 255)
        self.set_number(number)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
       
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()