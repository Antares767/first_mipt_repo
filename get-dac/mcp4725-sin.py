import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 1
sampling_frequency = 10


try:
        dac = mcp.MCP4725(5.000, address=0x61, verbose=True)
        start_time = time.perf_counter()
       
        while True:
            current_time = time.perf_counter() - start_time
            normalized = sg.get_sin_wave_amplitude(signal_frequency, current_time)
            voltage = normalized * amplitude

            dac.set_voltage(voltage)

            sg.wait_for_sampling_period(sampling_frequency)
            

finally:
    dac.deinit() 