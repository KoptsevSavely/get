import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac_pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac_pins, GPIO.OUT)
dynamic_range = 3.179

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    number = max(0, min(number, 255))
    binary_str = bin(number)[2:].zfill(8)
    binary_list = [int(bit) for bit in binary_str]
    for i in range(8):
        GPIO.output(dac_pins[i], binary_list[i])
    return binary_list

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            binary_output = number_to_dac(number)  # Сохраняем результат функции

            #print(f"Введите напряжение в Вольтах: {voltage}")
            print(f"Число на вход ЦАП: {number}, Бит: {binary_output}")
            print()

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

except KeyboardInterrupt:
    print("\nПрограмма завершена")

finally:
    GPIO.output(dac_pins, 0)
    GPIO.cleanup()
