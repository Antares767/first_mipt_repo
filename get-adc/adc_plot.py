import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage, color='blue', linewidth=2)
    plt.title("Зависимость напряжения от времени", fontsize=14)
    plt.xlabel("Время, с", fontsize=12)
    plt.ylabel("Напряжение, В", fontsize=12)
   
    if len(time) > 0:
        plt.xlim(0, time[-1] + 0.1)
    plt.ylim(0, max_voltage + 0.2)
   
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
   
    for i in range(1, len(time)):
        diff = time[i] - time[i-1]
        sampling_periods.append(diff)
       
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, color='green', edgecolor='black')
   
    plt.title("Распределение периодов измерений", fontsize=14)
    plt.xlabel("Период измерений, с", fontsize=12)
    plt.ylabel("Количество измерений", fontsize=12)
   
    plt.xlim(0, 0.06)
   
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()