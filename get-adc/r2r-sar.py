import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

if __name__ == "__main__":
    adc = R2R_ADC(dynamic_range=3.3, compare_time=0.0001, verbose=False)
   
    voltage_values = []
    time_values = []
    duration = 3.0
   
    try:
        start_time = time.time()
       
        while (time.time() - start_time) < duration:
            voltage = adc.get_sar_voltage()
            voltage_values.append(voltage)
            time_values.append(time.time() - start_time)
           
        plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
        plot_sampling_period_hist(time_values)
       
    except KeyboardInterrupt:
        pass
    finally:
        adc.deinit()