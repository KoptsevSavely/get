import mcp4725_driver
import signal_generator
import time

signal_frequency = 10
sampling_frequency = 100
dynamic_range = 3.3

if __name__ == "__main__":
    dac = None
    try:
        dac = mcp4725_driver.MCP4725(dynamic_range, verbose=False)
        start_time = time.time()
        
        while True:
            signal_generator.wait_for_sampling_period(sampling_frequency)
            current_time = time.time() - start_time
            voltage = signal_generator.get_sin_wave_amplitude(signal_frequency, current_time) * dynamic_range
            dac.set_voltage(voltage)
            
    except KeyboardInterrupt:
        print("\nОстановка генерации")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if dac:
            dac.deinit()