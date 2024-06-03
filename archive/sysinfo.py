from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QLabel, QPushButton)

import __init__

import main

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
        self.layout.addWidget(self.l_os, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_os_release, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_wm_de, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_hostname, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_cpu, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_arch, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_memory, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_swap, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_disk, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_user, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.l_uptime, alignment=Qt.AlignLeft)

        self.setLayout(self.layout)


    def set_appear(self):
        self.setWindowTitle("System Info")
        self.resize(700, 500)
        self.move(200, 100)


    def sysmon_click(self):
        main.sm.show()
        self.hide()

    def proc_click(self):
        main.pr.show()
        self.hide()

    
    def connects(self):
        self.btn_toproc.clicked.connect(self.proc_click)
        self.btn_tosysmon.clicked.connect(self.sysmon_click)
