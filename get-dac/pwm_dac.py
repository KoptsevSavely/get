import RPi.GPIO as GPIO
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        # Инициализация GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        
        # Создание объекта PWM
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        
        # Запуск ШИМ с заполнением 0%
        self.pwm.start(0)
        
        if self.verbose:
            print(f"PWM DAC инициализирован на пине {gpio_pin}")
            print(f"Частота ШИМ: {pwm_frequency} Гц")
            print(f"Динамический диапазон: 0.0 - {dynamic_range:.3f} В")
            print()
        
    def __deinit__(self):
        """Остановка ШИМ и очистка GPIO"""
        self.pwm.stop()  # Останавливаем ШИМ
        GPIO.cleanup()   # Освобождаем GPIO
        
        if self.verbose:
            print("PWM DAC остановлен, GPIO очищен")
    
    def set_voltage(self, voltage):

        # Проверка диапазона напряжения
        if voltage < 0:
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - 3.29 В)")
            voltage = 0.0
        elif voltage > self.dynamic_range:
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - 3.29 В)")
            voltage = self.dynamic_range
        
        # Расчет коэффициента заполнения (duty cycle)
        duty_cycle = (voltage / self.dynamic_range) * 100
        
        # Ограничение duty cycle от 0% до 100%
        duty_cycle = max(0, min(duty_cycle, 100))
        
        # Установка коэффициента заполнения
        self.pwm.ChangeDutyCycle(duty_cycle)
        
        if self.verbose:
            actual_voltage = duty_cycle * self.dynamic_range / 100
            
            # print(f"Запрошенное напряжение: {voltage:.3f} В")
            print(f"Коэффициент заполнения: {duty_cycle:.2f}")
            # print(f"Фактическое напряжение: {actual_voltage:.3f} В")
            
            print()
        
        return duty_cycle


if __name__ == "__main__":
    try:
        # Создание объекта PWM DAC
        dac = PWM_DAC(12, 900, 3.290, True)
        
        # Основной цикл программы
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