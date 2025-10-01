import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
        
    def __del__(self):
        self.deinit()

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        number = max(0, min(number, 255))
        
        binary_str = bin(number)[2:].zfill(8)
        binary_list = [int(bit) for bit in binary_str]
        
        for i in range(8):
            GPIO.output(self.gpio_bits[i], binary_list[i])
        
        if self.verbose:
            actual_voltage = number * self.dynamic_range / 255
            
            print(f"Число на вход ЦАП: {number}, Бит: {binary_list}")
            print()
        
        return binary_list

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.3f} В)")
            
            voltage = 0.0
        
        number = int(voltage / self.dynamic_range * 255)
        
        return self.set_number(number)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")
    
    finally:
        dac.deinit()