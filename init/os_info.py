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
        oss = f"{distro.name()}"
        os_release = f"{release()}"
        de_wm = f"{os.environ['DESKTOP_SESSION']}"

        # hostname
        with open("/etc/hostname", "r") as f:
            hostname = f"{f.read()}"

        # cpu
        cpu = f"{cpuinfo.get_cpu_info()['brand_raw']}"

        # arch
        arch = f"{cpuinfo.get_cpu_info()['arch']}"

        # memory
        memory = f"{psutil.virtual_memory().total // (1024 * 1024)} MB"

        # swap
        swap = f"{psutil.swap_memory().total // (1024 * 1024)} MB"

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

        disk = f"{txt_disk}"

        # user
        user = f"{getpass.getuser()}"

        # uptime
        seconds = time.time() - psutil.boot_time()
        uptime = f"{time.strftime('%H:%M:%S', time.gmtime(seconds))}"

        return (oss, os_release, de_wm, hostname, cpu, arch, memory, swap, disk, user, uptime)


    elif os_system == "Windows":
        # init os
        oss = f"{system()}"
        os_release = f"{release()}"
        de_wm = "Windows Shell"

        # hostname
        hostname = f"{socket.gethostname()}"

        # cpu
        cpu = f"{cpuinfo.get_cpu_info()['brand_raw']}"

        # arch
        arch = f"{cpuinfo.get_cpu_info()['arch']}"

        # memory
        memory = f"{psutil.virtual_memory().total // (1024 * 1024)} MB"

        # swap
        swap = f"{psutil.swap_memory().total // (1024 * 1024)} MB"

        # disk
        disk = []
        txt_disk = ""
        parts = psutil.disk_partitions()
        for part in parts:
            info = f"{part.device} ({part.mountpoint}) - {psutil.disk_usage(part.mountpoint).total // (1024 * 1024 * 1000)} GB\n"
            disk.append(info)

        for i in disk:
            txt_disk += i

        disk = f"{txt_disk}"

        # user
        user = f"{getpass.getuser()}"

        # uptime
        seconds = time.time() - psutil.boot_time()
        uptime = time.strftime('%H:%M:%S', time.gmtime(seconds))

        return (oss, os_release, de_wm, hostname, cpu, arch, memory, swap, disk, user, uptime)

    else:
        return False