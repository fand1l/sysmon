from platform import platform, system
import os
import psutil

os_system = system()

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