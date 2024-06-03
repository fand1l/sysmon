from PyQt6.QtCore import Qt, QTimer, QTime, QLocale
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QFont  # перевірка типів значень, що вводяться
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit,
    QTableWidgetItem, QTableWidget, QProgressBar)

import __init__
import time
import threading

css_path = "archive/sytle.css"



class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.InitUI()
        self.connects()
        self.show()

    def InitUI(self):
        self.btn_start = QPushButton("Почати")
        self.btn_start.setEnabled(False)
        self.l_init = QLabel("Перевірка системи. Зачекайте...")
        self.l_ready = QLabel("")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.l_init, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.l_ready, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.btn_start, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)

    def initsys(self):
        os = __init__.os_init()

        if not os:
            self.l_ready.setText("Ця система не підтримується!")

        else:
            self.l_ready.setText("Готово! Можна починати роботу")
            self.btn_start.setEnabled(True)


    def next_click(self):
        self.si = SysInfo()
        self.hide()


    def connects(self):
        self.btn_start.clicked.connect(self.next_click)

    
    def set_appear(self):
        self.setWindowTitle("Перевірка системи")
        self.resize(700, 500)
        self.move(200, 100)



class SysInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.InitUI()
        self.connects()
        self.show()


    def InitUI(self):
        self.btn_toproc = QPushButton("Процесси")
        self.btn_tosysmon = QPushButton("Системний монітор")
        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(self.btn_toproc)
        self.Hlayout.addWidget(self.btn_tosysmon)

        system = __init__.os_init()
        self.l_os = QLabel(system[0])
        self.l_os_release = QLabel(system[1])
        self.l_wm_de = QLabel(system[2])
        self.l_hostname = QLabel(system[3])
        self.l_cpu = QLabel(system[4])
        self.l_arch = QLabel(system[5])
        self.l_memory = QLabel(system[6])
        self.l_swap = QLabel(system[7])
        self.l_disk = QLabel(system[8])
        self.l_user = QLabel(system[9])
        self.l_uptime = QLabel(system[10])

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.l_os, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_os_release, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_wm_de, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_hostname, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_cpu, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_arch, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_memory, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_swap, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_disk, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_user, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.l_uptime, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.layout)


    def set_appear(self):
        self.setWindowTitle("System Info")
        self.resize(700, 500)
        self.move(200, 100)


    def sysmon_click(self):
        self.sm = SysMon()
        #self.sm.show()
        self.hide()

    def proc_click(self):
        self.pr = Proc()
        #self.pr.show()
        self.hide()

    
    def connects(self):
        self.btn_toproc.clicked.connect(self.proc_click)
        self.btn_tosysmon.clicked.connect(self.sysmon_click)



class SysMon(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.InitUI()
        self.connects()
        self.show()
        self.start_thread()

    
    def InitUI(self):
        self.btn_toproc = QPushButton("Процесси")
        self.btn_tosysinfo = QPushButton("Системна інформація")
        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(self.btn_toproc)
        self.Hlayout.addWidget(self.btn_tosysinfo)

        system = __init__.monitor()
        self.Vlayout1 = QVBoxLayout()
        
        self.l_cpu_percent_global = QLabel(system[0])
        self.l_cpu_percent = QLabel(system[1])
        self.l_mem_usage = QLabel(system[2])
        self.l_swap_usage = QLabel(system[3])
        self.l_disk_usage = QLabel(system[4])
        self.l_temp = QLabel(system[5])
        self.l_fans = QLabel(system[6])

        self.Vlayout1.addWidget(self.l_cpu_percent_global)
        self.Vlayout1.addWidget(self.l_cpu_percent)
        self.Vlayout1.addWidget(self.l_mem_usage)
        self.Vlayout1.addWidget(self.l_swap_usage)
        self.Vlayout1.addWidget(self.l_disk_usage)
        self.Vlayout1.addWidget(self.l_temp)
        self.Vlayout1.addWidget(self.l_fans)
        #self.l_choose = QLabel("Оберіть датчик!")

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.Hlayout)
        #self.layout.addWidget(self.l_choose, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.Vlayout1)

        self.setLayout(self.layout)
        

    def new_data(self):
        system = __init__.monitor()

        self.l_cpu_percent_global.setText(system[0])
        self.l_cpu_percent.setText(system[1])
        self.l_mem_usage.setText(system[2])
        self.l_swap_usage.setText(system[3])
        self.l_disk_usage.setText(system[4])
        self.l_temp.setText(system[5])
        self.l_fans.setText(system[6])


    def set_appear(self):
        self.setWindowTitle("System Monitor")
        self.resize(700, 500)
        self.move(200, 100)


    def sysinfo_click(self):
        self.si = SysInfo()
        self.hide()


    def proc_click(self):
        self.pr = Proc()
        #self.pr.show()
        self.hide()

    
    def connects(self):
        self.btn_toproc.clicked.connect(self.proc_click)
        self.btn_tosysinfo.clicked.connect(self.sysinfo_click)

    
    def start_thread(self):
        thread = threading.Thread(target=self.new_data_thread)
        thread.start()


    def new_data_thread(self):
        while True:
            self.new_data()
            threading.Event().wait(3)



class Proc(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.InitUI()
        self.connects()
        self.show()

    def InitUI(self):
        self.btn_tosysmon = QPushButton("Системний монітор")
        self.btn_tosysinfo = QPushButton("Системна інформація")
        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(self.btn_tosysmon)
        self.Hlayout.addWidget(self.btn_tosysinfo)

        processes = __init__.procces()

        #self.scroll = QScrollArea()
        self.table = QTableWidget()
        #self.scroll.addWidget(self.table)
        self.table.setColumnCount(2)
        self.table.setRowCount(len(processes)+1)
        self.table.setItem(0, 0, QTableWidgetItem("Name"))
        self.table.setItem(0, 1, QTableWidgetItem("user"))

        i = 0
        for proc in processes:
            self.table.setItem(i, 0, QTableWidgetItem(proc["name"]))
            self.table.setItem(i, 1, QTableWidgetItem(proc["username"]))

            i += 1

        for i in range(self.table.columnCount()):
            self.table.resizeColumnToContents(i)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)


    def set_appear(self):
        self.setWindowTitle("Procces Monitor")
        self.resize(700, 500)
        self.move(200, 100)


    def sysmon_click(self):
        self.sm = SysMon()
        self.hide()


    def sysinfo_click(self):
        self.si = SysInfo()
        self.hide()

    
    def connects(self):
        self.btn_tosysmon.clicked.connect(self.sysmon_click)
        self.btn_tosysinfo.clicked.connect(self.sysinfo_click)



def main():
    app = QApplication([])
    with open(css_path, "r") as f:
        app.setStyleSheet(f.read())
    mw = MainWin()

    mw.initsys()
    app.exec()

if __name__ == "__main__":
    main()
