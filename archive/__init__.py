from platform import platform, system, release, processor, architecture
import os
import psutil
import getpass
import time
import cpuinfo
import distro
import socket

os_system = system()

def os_init():
    if os_system == "Linux":
        # init os
        oss = f"Дистрибутив: {distro.name()}"
        os_release = f"Версія ядра: {release()}"
        de_wm = f"Віконний менеджер: {os.environ['DESKTOP_SESSION']}"

        # hostname
        with open("/etc/hostname", "r") as f:
            hostname = f"Хост: {f.read()}"

        # cpu
        cpu = f"Процессор: {cpuinfo.get_cpu_info()['brand_raw']}"

        # arch
        arch = f"Архітектура: {cpuinfo.get_cpu_info()['arch']}"

        # memory
        memory = f"ОЗП: {psutil.virtual_memory().total // (1024 * 1024)} MB"

        # swap
        swap = f"SWAP ОЗП: {psutil.swap_memory().total // (1024 * 1024)} MB"

        # disk
        disk = []
        txt_disk = ""
        parts = psutil.disk_partitions()
        for part in parts:
            info = f"{part.device} ({part.mountpoint}) - {psutil.disk_usage(part.mountpoint).total // (1024 * 1024 * 1000)} GB\n"
            if not part.device.startswith("/dev/loop"):
                disk.append(info)

        for i in disk:
            txt_disk += i

        disk = f"Розділи/томи: {txt_disk}"

        # user
        user = f"Користувач: {getpass.getuser()}"

        # uptime
        seconds = time.time() - psutil.boot_time()
        uptime = f"Час роботи: {time.strftime('%H:%M:%S', time.gmtime(seconds))}"

        return (oss, os_release, de_wm, hostname, cpu, arch, memory, swap, disk, user, uptime)


    elif os_system == "Windows":
        # init os
        oss = f"Операційна система: {system()}"
        os_release = f"Версія ОС: {release()}"
        de_wm = "Віконний менеджер: Windows Shell"

        # hostname
        hostname = f"Хост: {socket.gethostname()}"

        # cpu
        cpu = f"Процессор: {cpuinfo.get_cpu_info()['brand_raw']}"

        # arch
        arch = f"Архітектура: {cpuinfo.get_cpu_info()['arch']}"

        # memory
        memory = f"ОЗП: {psutil.virtual_memory().total // (1024 * 1024)} MB"

        # swap
        swap = f"SWAP ОЗП: Не доступно для Windows"

        # disk
        disk = []
        txt_disk = ""
        parts = psutil.disk_partitions()
        for part in parts:
            info = f"{part.device} ({part.mountpoint}) - {psutil.disk_usage(part.mountpoint).total // (1024 * 1024 * 1000)} GB\n"
            disk.append(info)

        for i in disk:
            txt_disk += i

        disk = f"Розділи/томи: {txt_disk}"

        # user
        user = f"Користувач: {getpass.getuser()}"

        # uptime
        seconds = time.time() - psutil.boot_time()
        uptime = f"Час роботи: {time.strftime('%H:%M:%S', time.gmtime(seconds))}"

        return (oss, os_release, de_wm, hostname, cpu, arch, memory, swap, disk, user, uptime)

    else:
        return False


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
            txt_cpus += f"Ядро {i}: {cpus[i]}%\n"
        cpu_percent_global = f"Процессори: \n{txt_cpus}"
        cpu_percent = f"Процессор (середнє): {psutil.cpu_percent(interval=1, percpu=False)}%"

        # mem usage
        st = psutil.virtual_memory().total
        sa = psutil.virtual_memory().available
        mem_usage = f"ОЗП: {round(((st - sa) / st * 100), 1)}%"

        # swap usage
        swap_usage = f"SWAP ОЗП: Недоступно для Windows"

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

        #fans
        fan = f"Кулери: Недоступно для Windows"
        return (cpu_percent_global, cpu_percent, mem_usage, swap_usage, disk_usage, temp, fan, cpu_percent_int)

    else:
        return False


def procces():
    if os_system == "Linux":
        # get all procces
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            processes.append(proc.info)

        return processes

    elif os_system == "Windows":
        # get all procces
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            processes.append(proc.info)

        return processes

    else:
        return False