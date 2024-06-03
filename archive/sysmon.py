from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QLabel, QPushButton)

import __init__
from main import *

class SysMon(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.InitUI()
        self.connects()
        self.show()

    
    def InitUI(self):
        self.btn_toproc = QPushButton("Процесси")
        self.btn_tosysinfo = QPushButton("Системна інформація")
        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(self.btn_toproc)
        self.Hlayout.addWidget(self.btn_tosysinfo)

        system = __init__.monitor()
        self.l_cpu_percent_global = QLabel(system[0])
        self.l_cpus_percent = QLabel(system[1])
        self.l_mem_usage = QLabel(system[2])
        self.l_swap_usage = QLabel(system[3])
        self.l_disk_usage = QLabel(system[4])
        self.l_temp = QLabel(system[5])
        self.l_fans = QLabel(system[6])

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.l_cpu_percent_global, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_cpus_percent, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_mem_usage, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_swap_usage, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_disk_usage, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_temp, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_fans, alignment=Qt.AlignLeft)

        self.setLayout(self.layout)


    def set_appear(self):
        self.setWindowTitle("System Monitor")
        self.resize(700, 500)
        self.move(200, 100)


    def sysinfo_click(self):
        try:
            self.si = SysInfo()
        except:
            self.si.show()
        self.hide()


    def proc_click(self):
        try:
            self.pr = Proc()
        except:
            self.pr.show()
        self.hide()

    
    def connects(self):
        self.btn_toproc.clicked.connect(self.proc_click)
        self.btn_tosysinfo.clicked.connect(self.sysinfo_click)