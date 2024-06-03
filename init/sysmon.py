from platform import platform, system, release, processor, architecture
import os
import psutil
import getpass
import time
import cpuinfo
import distro
import socket

os_system = system()

def monitor():
    if os_system == "Linux":
        # cpu percent
        cpus = psutil.cpu_percent(interval=1, percpu=True)
        txt_cpus = ""
        for i in range(len(cpus)):
            txt_cpus += f"Ядро {i}: {cpus[i]}%\n"
        cpu_percent_global = f"Процессори: \n{txt_cpus}"

        cpu_percent_int = psutil.cpu_percent(interval=1, percpu=False)
        cpu_percent = f"Процессор (середнє): {cpu_percent_int}%"

        # mem usage
        st = psutil.virtual_memory().total
        sa = psutil.virtual_memory().available
        mem_usage = f"ОЗП: {round(((st - sa) / st * 100), 1)}%"

        # swap usage
        st = psutil.swap_memory().total
        sa = psutil.swap_memory().free
        swap_usage = f"SWAP ОЗП: {round(((st - sa) / st * 100), 1)}%"

        # disk usage
        st = psutil.disk_usage('/').total
        sa = psutil.disk_usage('/').free
        disk_usage = f"Диск: {round(((st - sa) / st * 100), 1)}%"

        # temp
        c0 = psutil.sensors_temperatures()["coretemp"][1].current
        c1 = psutil.sensors_temperatures()["coretemp"][2].current
        c2 = psutil.sensors_temperatures()["coretemp"][3].current
        c3 = psutil.sensors_temperatures()["coretemp"][4].current

        temp = f"Температура процессора: {sum([c0, c1, c2, c3]) / 4} °C"

        # fans
        fan = ""
        fans = psutil.sensors_fans()
        for name, entries in fans.items():
            for entry in entries:
                fan += '   %-10s %s RPM' % (entry.label or name, entry.current)

        fan = f"Кулери: {fan}"
        return (cpu_percent_global, cpu_percent, mem_usage, swap_usage, disk_usage, temp, fan, cpu_percent_int)


    elif os_system == "Windows":
        # cpu percent
        cpus = psutil.cpu_percent(interval=1, percpu=True)
        txt_cpus = ""
        for i in range(len(cpus)):
            txt_cpus += f"{i}: {cpus[i]}%\n"
        cpu_percent_global = f"{txt_cpus}"
        cpu_percent = f"{psutil.cpu_percent(interval=1, percpu=False)}%"

        # mem usage
        st = psutil.virtual_memory().total
        sa = psutil.virtual_memory().available
        mem_usage = f"{round(((st - sa) / st * 100), 1)}%"

        # swap usage
        swap_usage = f"" # !!!

        # disk usage
        st = psutil.disk_usage('/').total
        sa = psutil.disk_usage('/').free
        disk_usage = f"{round(((st - sa) / st * 100), 1)}%"

        # temp
        c0 = psutil.sensors_temperatures()["coretemp"][1].current
        c1 = psutil.sensors_temperatures()["coretemp"][2].current
        c2 = psutil.sensors_temperatures()["coretemp"][3].current
        c3 = psutil.sensors_temperatures()["coretemp"][4].current

        temp = f"{sum([c0, c1, c2, c3]) / 4} °C"

        #fans
        fan = "Недоступно для Windows"
        return (cpu_percent_global, cpu_percent, mem_usage, swap_usage, disk_usage, temp, fan, cpu_percent_int)

    else:
        return False