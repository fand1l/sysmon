from platform import platform, system
import os
import psutil
import time

os_system = system()

def monitor():
    if os_system == "Linux":
        # cpu percent
        cpu_percent_int = psutil.cpu_percent(interval=0, percpu=False)

        # mem usage
        st = psutil.virtual_memory().total
        sa = psutil.virtual_memory().available
        mem_usage = round(((st - sa) / st * 100), 1)

        # swap usage
        st = psutil.swap_memory().total
        sa = psutil.swap_memory().free
        swap_usage = round(((st - sa) / st * 100), 1)

        # network
        net_io_start = psutil.net_io_counters()

        time.sleep(0.7)

        net_io_end = psutil.net_io_counters()

        bytes_sent = (net_io_end.bytes_sent - net_io_start.bytes_sent) // 1048576
        bytes_recv = (net_io_end.bytes_recv - net_io_start.bytes_recv) // 1048576

        # temp
        c0 = psutil.sensors_temperatures()["coretemp"][1].current
        c1 = psutil.sensors_temperatures()["coretemp"][2].current
        c2 = psutil.sensors_temperatures()["coretemp"][3].current
        c3 = psutil.sensors_temperatures()["coretemp"][4].current

        temp = sum([c0, c1, c2, c3]) / 4

        return (cpu_percent_int, mem_usage, swap_usage, bytes_sent, bytes_recv, temp)


    elif os_system == "Windows":
        # cpu percent
        cpu_percent_int = psutil.cpu_percent(interval=1, percpu=False)

        # mem usage
        st = psutil.virtual_memory().total
        sa = psutil.virtual_memory().available
        mem_usage = round(((st - sa) / st * 100), 1)

        # swap usage
        st = psutil.swap_memory().total
        sa = psutil.swap_memory().free
        swap_usage = round(((st - sa) / st * 100), 1)

        # network
        net_io_start = psutil.net_io_counters()

        time.sleep(1)

        net_io_end = psutil.net_io_counters()

        bytes_sent = net_io_end.bytes_sent - net_io_start.bytes_sent
        bytes_recv = net_io_end.bytes_recv - net_io_start.bytes_recv

        # temp
        c0 = psutil.sensors_temperatures()["coretemp"][1].current
        c1 = psutil.sensors_temperatures()["coretemp"][2].current
        c2 = psutil.sensors_temperatures()["coretemp"][3].current
        c3 = psutil.sensors_temperatures()["coretemp"][4].current

        temp = sum([c0, c1, c2, c3]) / 4

        return (cpu_percent_int, mem_usage, swap_usage, bytes_sent, bytes_recv, temp)

    else:
        return False