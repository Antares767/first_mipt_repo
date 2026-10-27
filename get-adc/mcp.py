import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

if __name__ == "__main__":
    adc = MCP3021(dynamic_range=5.0, verbose=False)
   
    voltage_values = []
    time_values = []
    duration = 3.0
   
    try:
        start_time = time.time()
       
        while (time.time() - start_time) < duration:
            voltage = adc.get_voltage()
            voltage_values.append(voltage)
            time_values.append(time.time() - start_time)
           
        plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
        plot_sampling_period_hist(time_values)
       
    except KeyboardInterrupt:
        pass
    finally:
        adc.deinit()