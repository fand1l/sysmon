from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QLabel, QPushButton, QScrollArea,
    QTableWidget, QTableWidgetItem)

import __init__

from main import *

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

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)


    def set_appear(self):
        self.setWindowTitle("Procces Monitor")
        self.resize(700, 500)
        self.move(200, 100)


    def sysmon_click(self):
        try:
            self.sm = SysMon()
        except:
            self.sm.show()
        self.hide()


    def sysinfo_click(self):
        try:
            self.si = SysInfo()
        except:
            self.si.show()
        self.hide()

    
    def connects(self):
        self.btn_tosysmon.clicked.connect(self.sysmon_click)
        self.btn_tosysinfo.clicked.connect(self.sysinfo_click)