import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def number_to_dac(self, number):
        number = max(0, min(int(number), 255))
        states = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, states)

        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {states}")

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
           
            time.sleep(self.compare_time)
           
            comp_state = GPIO.input(self.comp_gpio)
           
            if self.verbose:
                print(f"Проверка: ЦАП = {number}, Компаратор = {comp_state}")

            if comp_state == 1:
                return number
               
        return 255

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = (number / 255.0) * self.dynamic_range
        return voltage

    def successive_approximation_adc(self):
        result = 0
        for bit in range(7, -1, -1):
            test_result = result | (1 << bit)
            self.number_to_dac(test_result)
            time.sleep(self.compare_time)
            
            if GPIO.input(self.comp_gpio) == 0:
                result = test_result
                
        return result

    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        return (number / 255.0) * self.dynamic_range

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def __del__(self):
        try:
            GPIO.output(self.bits_gpio, 0)
        except:
            pass


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3, verbose=False)
       
        while True:
            # voltage = adc.get_sc_voltage()
            voltage = adc.get_sar_voltage()
            print(f"Напряжение: {voltage:.2f} В")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем")
    finally:
        adc.deinit()