import sys
from PySide6.QtWidgets import (
            QApplication, QMainWindow, QWidget,
            QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
            QTableWidget, QTableWidgetItem
            )
from PySide6.QtCore import QFile, QThread, Signal, Qt
from PySide6.QtGui import QFont
from UI.ui_mainwindow import Ui_MainWindow
import pyqtgraph as pg
import time
from sys import path as project_path

import init.os_info
import init.proc
import init.sysmon

style_css_path = f"{project_path[0]}/style.css"


class DataThread(QThread):
    os_ready = Signal(str)

    os_name = Signal(str)
    os_release = Signal(str)
    os_dewm = Signal(str)
    os_user = Signal(str)
    os_host = Signal(str)
    os_cpu = Signal(str)
    os_arch = Signal(str)
    os_memory = Signal(str)
    os_swap = Signal(str)
    os_partitions = Signal(str)
    os_uptime = Signal(str)

    mon_cpu_percent = Signal(float)
    mon_memory = Signal(float)
    mon_swap = Signal(float)
    mon_sent = Signal(float)
    mon_recv = Signal(float)
    mon_temp = Signal(float)

    pr_proc = Signal(list)

    def run(self):
        while True:
            os_i = init.os_info.os_init()
            os_m = init.sysmon.monitor()
            os_p = init.proc.procces()
            os_system = init.os_info.os_system
            time.sleep(2)
            if os_i:
                if os_system == "Linux":
                    # OS READY
                    self.os_ready.emit(f"Вітаю, {os_i[9]}! Ваша операційна система {os_i[0]} повністю підтримується!")
                    
                    # OS INFO
                    self.os_name.emit(f"Дистрибутив: {os_i[0]}")
                    self.os_release.emit(f"Версія ядра: {os_i[1]}")
                    self.os_dewm.emit(f"Графічна оболонка: {os_i[2]}")
                    self.os_user.emit(f"Користувач: {os_i[9]}")
                    self.os_host.emit(f"Пристрій: {os_i[3]}")
                    self.os_cpu.emit(f"Центральний процесор: {os_i[4]}")
                    self.os_arch.emit(f"Архітектура: {os_i[5]}")
                    self.os_memory.emit(f"Оперативна пам'ять: {os_i[6]}")
                    self.os_swap.emit(f"Резервна пам'ять (swap): {os_i[7]}")
                    self.os_partitions.emit(f"Розділи диску:\n{os_i[8]}")
                    self.os_uptime.emit(f"Час роботи: {os_i[10]}")

                    # SYSTEM MONITOR
                    self.mon_cpu_percent.emit(os_m[0])
                    self.mon_memory.emit(os_m[1])
                    self.mon_swap.emit(os_m[2])
                    self.mon_sent.emit(os_m[3])
                    self.mon_recv.emit(os_m[4])
                    self.mon_temp.emit(os_m[5])

                    # PROC
                    self.pr_proc.emit(os_p)
                
                elif os_system == "Windows":
                    self.os_ready.emit(f"Вітаю, {os_i[9]}! Ваша операційна система {os_i[0]} {os_i[1]} частково підтримується!")

                    # OS INFO
                    self.os_name.emit(f"Операційна система: {os_i[0]}")
                    self.os_release.emit(f"Реліз: {os_i[1]}")
                    self.os_dewm.emit(f"Графічна оболонка: {os_i[2]}")
                    self.os_user.emit(f"Користувач: {os_i[9]}")
                    self.os_host.emit(f"Пристрій: {os_i[3]}")
                    self.os_cpu.emit(f"Центральний процесор: {os_i[4]}")
                    self.os_arch.emit(f"Архітектура: {os_i[5]}")
                    self.os_memory.emit(f"Оперативна пам'ять: {os_i[6]}")
                    self.os_swap.emit(f"Резервна пам'ять (swap): {os_i[7]}")
                    self.os_partitions.emit(f"Томи диску:\n{os_i[8]}")
                    self.os_uptime.emit(f"Час роботи: {os_i[10]}")

                    # SYSTEM MONITOR
                    self.mon_cpu_percent.emit(os_m[0])
                    self.mon_memory.emit(os_m[1])
                    self.mon_swap.emit(os_m[2])
                    self.mon_sent.emit(os_m[3])
                    self.mon_recv.emit(os_m[4])
                    self.mon_temp.emit(os_m[5])

                    # PROC
                    self.pr_proc.emit(os_p)
                
                else:
                    self.os_ready.emit(f"Нажаль ваша операційна система не підтримується")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect()

        self.system_monitor = System_Monitor(self)

        self.w_os_ready = OS_Ready()
        self.w_os_info = OS_Info()
        self.w_sysmon = System_Monitor(self)
        self.w_proc = Proc()
        self.w_settings = Settings()

        self.ui.content_swidget.addWidget(self.w_os_ready)
        self.ui.content_swidget.addWidget(self.w_os_info)
        self.ui.content_swidget.addWidget(self.w_proc)
        self.ui.content_swidget.addWidget(self.w_sysmon)
        self.ui.content_swidget.addWidget(self.w_settings)

        self.ui.content_swidget.setCurrentWidget(self.w_os_ready)

    def connect(self):
        self.ui.btn_settings.clicked.connect(lambda: self.ui.content_swidget.setCurrentWidget(self.w_settings))
        self.ui.btn_sysmon.clicked.connect(lambda: self.ui.content_swidget.setCurrentWidget(self.w_sysmon))
        self.ui.btn_proc.clicked.connect(lambda: self.ui.content_swidget.setCurrentWidget(self.w_proc))
        self.ui.btn_sysinfo.clicked.connect(lambda: self.ui.content_swidget.setCurrentWidget(self.w_os_info))


class OS_Ready(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

        self.data_thread = DataThread()
        self.data_thread.os_ready.connect(self.update)
        self.data_thread.start()

    def InitUI(self):
        self.l_ready_os = QLabel("Завантаження данних про операційну систему!")
        self.v_layout = QVBoxLayout()
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.l_ready_os.setFont(font)
        self.v_layout.addWidget(self.l_ready_os, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)

    def update(self, data):
        self.l_ready_os.setText(data)
        

class OS_Info(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        
        self.data_thread = DataThread()
        self.data_thread.os_name.connect(self.update_name)
        self.data_thread.os_release.connect(self.update_release)
        self.data_thread.os_dewm.connect(self.update_dewm)
        self.data_thread.os_user.connect(self.update_user)
        self.data_thread.os_host.connect(self.update_host)
        self.data_thread.os_cpu.connect(self.update_cpu)
        self.data_thread.os_arch.connect(self.update_arch)
        self.data_thread.os_memory.connect(self.update_memory)
        self.data_thread.os_swap.connect(self.update_swap)
        self.data_thread.os_partitions.connect(self.update_partitions)
        self.data_thread.os_uptime.connect(self.update_uptime)
        self.data_thread.start()

    def InitUI(self):
        self.l_hardware = QLabel("Дані щодо обладнання")
        self.l_software = QLabel("Дані щодо програмного забезпечення")
        self.l_other = QLabel("Інше")

        font = QFont()
        font.setPointSize(16)
        font.setBold(True)

        self.l_hardware.setFont(font)
        self.l_software.setFont(font)
        self.l_other.setFont(font)

        self.l_name = QLabel("Завантаження інформації")
        self.l_release = QLabel("Завантаження інформації")
        self.l_dewm = QLabel("Завантаження інформації")
        self.l_user = QLabel("Завантаження інформації")
        self.l_host = QLabel("Завантаження інформації")
        self.l_cpu = QLabel("Завантаження інформації")
        self.l_arch = QLabel("Завантаження інформації")
        self.l_memory = QLabel("Завантаження інформації")
        self.l_swap = QLabel("Завантаження інформації")
        self.l_partitions = QLabel("Завантаження інформації")
        self.l_uptime = QLabel("Завантаження інформації")



        self.v_layout = QVBoxLayout() # ALL
        self.h1_layout = QHBoxLayout() # SOFT + HARD
        self.h2_layout = QHBoxLayout() # ONLY OTHER
        self.v2_layout = QVBoxLayout() # HARD
        self.v3_layout = QVBoxLayout() # SOFT
        self.v4_layout = QVBoxLayout() # OTHER

        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addLayout(self.h2_layout)
        self.h1_layout.addLayout(self.v2_layout)
        self.h1_layout.addLayout(self.v3_layout)
        self.h2_layout.addLayout(self.v4_layout)

        self.v2_layout.addWidget(self.l_hardware, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v3_layout.addWidget(self.l_software, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v4_layout.addWidget(self.l_other, alignment=Qt.AlignmentFlag.AlignCenter)

        self.v3_layout.addWidget(self.l_name, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v3_layout.addWidget(self.l_release, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v3_layout.addWidget(self.l_dewm, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v3_layout.addWidget(self.l_user, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v3_layout.addWidget(self.l_host, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_cpu, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_arch, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_memory, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_swap, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_partitions, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v4_layout.addWidget(self.l_uptime, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)

    def update_name(self, data):
        self.l_name.setText(data)

    def update_release(self, data):
        self.l_release.setText(data)

    def update_dewm(self, data):
        self.l_dewm.setText(data)

    def update_user(self, data):
        self.l_user.setText(data)

    def update_host(self, data):
        self.l_host.setText(data)

    def update_cpu(self, data):
        self.l_cpu.setText(data)

    def update_arch(self, data):
        self.l_arch.setText(data)

    def update_memory(self, data):
        self.l_memory.setText(data)

    def update_swap(self, data):
        self.l_swap.setText(data)

    def update_partitions(self, data):
        self.l_partitions.setText(data)

    def update_uptime(self, data):
        self.l_uptime.setText(data)


class System_Monitor(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.InitUI()
        self.connects()

        self.w_cpu = SM_CPU(self.main_window, self)
        self.w_mem = SM_MEM(self.main_window, self)
        self.w_net = SM_NET(self.main_window, self)

        self.main_window.ui.content_swidget.addWidget(self.w_cpu)
        self.main_window.ui.content_swidget.addWidget(self.w_mem)
        self.main_window.ui.content_swidget.addWidget(self.w_net)

    def InitUI(self):
        self.btn_cpu = QPushButton("ЦП")
        self.btn_memory = QPushButton("ОЗП")
        self.btn_network = QPushButton("Мережа")

        self.l_welcome = QLabel("Оберіть датчик за яким будете слідкувати")

        self.v_layout = QVBoxLayout()
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.l_welcome.setFont(font)

        self.h1_layout = QHBoxLayout() # For information
        self.h2_layout = QHBoxLayout() # For buttons

        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addLayout(self.h2_layout)

        self.h2_layout.addWidget(self.btn_cpu)
        self.h2_layout.addWidget(self.btn_memory)
        self.h2_layout.addWidget(self.btn_network)

        self.h1_layout.addWidget(self.l_welcome, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)

    def connects(self):
        self.btn_cpu.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.w_cpu))
        self.btn_memory.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.w_mem))
        self.btn_network.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.w_net))


class SM_CPU(QWidget):
    def __init__(self, main_window, sysmon):
        super().__init__()
        self.main_window = main_window
        self.sysmon = sysmon
        self.InitUI()
        self.connects()

        self.data_thread = DataThread()
        self.data_thread.mon_cpu_percent.connect(self.update_cpu)
        self.data_thread.mon_temp.connect(self.update_temp)
        self.data_thread.start()

    def InitUI(self):
        self.btn_cpu = QPushButton("ЦП")
        self.btn_memory = QPushButton("ОЗП")
        self.btn_network = QPushButton("Мережа")

        self.l_info_cpu = QLabel("Завантаження")
        self.l_info_temp = QLabel("Завантаження")

        # CPU
        self.cpu_plot_widget = pg.PlotWidget()
        self.cpu_plot_widget.setYRange(0, 100)
        self.cpu_plot_widget.setLabel('left', 'CPU Usage (%)')
        self.cpu_plot_widget.setLabel('bottom', 'Time (s)')
        self.cpu_plot_widget.setFixedHeight(150)

        self.cpu_data = []
        self.cpu_curve = self.cpu_plot_widget.plot(self.cpu_data, pen='g')

        # Temp
        self.temp_plot_widget = pg.PlotWidget()
        self.temp_plot_widget.setYRange(0, 110)
        self.temp_plot_widget.setLabel('left', 'Temp (°C)')
        self.temp_plot_widget.setLabel('bottom', 'Time (s)')
        self.temp_plot_widget.setFixedHeight(150)

        self.temp_data = []
        self.temp_curve = self.temp_plot_widget.plot(self.temp_data, pen='b')

        self.v_layout = QVBoxLayout()

        self.h1_layout = QHBoxLayout() # For information
        self.h2_layout = QHBoxLayout() # For buttons

        self.v2_layout = QVBoxLayout()

        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addLayout(self.h2_layout)

        self.h2_layout.addWidget(self.btn_cpu)
        self.h2_layout.addWidget(self.btn_memory)
        self.h2_layout.addWidget(self.btn_network)

        self.h1_layout.addLayout(self.v2_layout)
        self.v2_layout.addWidget(self.l_info_cpu, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.cpu_plot_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_info_temp, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.temp_plot_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)

    def update_cpu(self, data):
        self.l_info_cpu.setText(f"Центральний процесор: {data}%")
        self.cpu_data.append(data)
        if len(self.cpu_data) > 80:
            self.cpu_data.pop(0)
        self.cpu_curve.setData(self.cpu_data)

    def update_temp(self, data):
        self.l_info_temp.setText(f"Температура ЦП: {data} °C")
        self.temp_data.append(data)
        if len(self.temp_data) > 80:
            self.temp_data.pop(0)
        self.temp_curve.setData(self.temp_data)


    def connects(self):
        self.btn_cpu.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_cpu))
        self.btn_memory.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_mem))
        self.btn_network.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_net))


class SM_MEM(QWidget):
    def __init__(self, main_window, sysmon):
        super().__init__()
        self.main_window = main_window
        self.sysmon = sysmon
        self.InitUI()
        self.connects()

        self.data_thread = DataThread()
        self.data_thread.mon_memory.connect(self.update_mem)
        self.data_thread.mon_swap.connect(self.update_swap)
        self.data_thread.start()

    def InitUI(self):
        self.btn_cpu = QPushButton("ЦП")
        self.btn_memory = QPushButton("ОЗП")
        self.btn_network = QPushButton("Мережа")

        self.l_info_mem = QLabel("Завантаження")
        self.l_info_swap = QLabel("Завантаження")

        # MEM
        self.mem_plot_widget = pg.PlotWidget()
        self.mem_plot_widget.setYRange(0, 100)
        self.mem_plot_widget.setLabel('left', 'Memory Usage (%)')
        self.mem_plot_widget.setLabel('bottom', 'Time (s)')
        self.mem_plot_widget.setFixedHeight(150)

        self.mem_data = []
        self.mem_curve = self.mem_plot_widget.plot(self.mem_data, pen='g')

        # SWAP
        self.swap_plot_widget = pg.PlotWidget()
        self.swap_plot_widget.setYRange(0, 110)
        self.swap_plot_widget.setLabel('left', 'Swap Usage (%)')
        self.swap_plot_widget.setLabel('bottom', 'Time (s)')
        self.swap_plot_widget.setFixedHeight(150)

        self.swap_data = []
        self.swap_curve = self.swap_plot_widget.plot(self.swap_data, pen='b')

        self.v_layout = QVBoxLayout()

        self.h1_layout = QHBoxLayout() # For information
        self.h2_layout = QHBoxLayout() # For buttons

        self.v2_layout = QVBoxLayout()

        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addLayout(self.h2_layout)

        self.h2_layout.addWidget(self.btn_cpu)
        self.h2_layout.addWidget(self.btn_memory)
        self.h2_layout.addWidget(self.btn_network)

        self.h1_layout.addLayout(self.v2_layout)
        self.v2_layout.addWidget(self.l_info_mem, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.mem_plot_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_info_swap, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.swap_plot_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)

    def update_mem(self, data):
        self.l_info_mem.setText(f"Оперативна пам'ять: {data}%")
        self.mem_data.append(data)
        if len(self.mem_data) > 80:
            self.mem_data.pop(0)
        self.mem_curve.setData(self.mem_data)

    def update_swap(self, data):
        self.l_info_swap.setText(f"Резервна пам'ять (swap): {data}%")
        self.swap_data.append(data)
        if len(self.swap_data) > 80:
            self.swap_data.pop(0)
        self.swap_curve.setData(self.swap_data)

    def connects(self):
        self.btn_cpu.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_cpu))
        self.btn_memory.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_mem))
        self.btn_network.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_net))


class SM_NET(QWidget):
    def __init__(self, main_window, sysmon):
        super().__init__()
        self.main_window = main_window
        self.sysmon = sysmon
        self.InitUI()
        self.connects()

        self.data_thread = DataThread()
        self.data_thread.mon_sent.connect(self.update_sent)
        self.data_thread.mon_recv.connect(self.update_recv)
        self.data_thread.start()

    def InitUI(self):
        self.btn_cpu = QPushButton("ЦП")
        self.btn_memory = QPushButton("ОЗП")
        self.btn_network = QPushButton("Мережа")

        self.l_info_sent = QLabel("Завантаження")
        self.l_info_recv = QLabel("Завантаження")

        # Sent
        self.sent_plot_widget = pg.PlotWidget()
        self.sent_plot_widget.setLabel('left', 'Sent (%)')
        self.sent_plot_widget.setLabel('bottom', 'Time (s)')
        self.sent_plot_widget.setFixedHeight(150)

        self.sent_data = []
        self.sent_curve = self.sent_plot_widget.plot(self.sent_data, pen='b')

        # Recv
        self.recv_plot_widget = pg.PlotWidget()
        self.recv_plot_widget.setLabel('left', ' Receive (%)')
        self.recv_plot_widget.setLabel('bottom', 'Time (s)')
        self.recv_plot_widget.setFixedHeight(150)

        self.recv_data = []
        self.recv_curve = self.recv_plot_widget.plot(self.recv_data, pen='b')

        self.v_layout = QVBoxLayout()

        self.h1_layout = QHBoxLayout() # For information
        self.h2_layout = QHBoxLayout() # For buttons

        self.v2_layout = QVBoxLayout()

        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addLayout(self.h2_layout)

        self.h2_layout.addWidget(self.btn_cpu)
        self.h2_layout.addWidget(self.btn_memory)
        self.h2_layout.addWidget(self.btn_network)

        self.h1_layout.addLayout(self.v2_layout)
        self.v2_layout.addWidget(self.l_info_sent, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.sent_plot_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.l_info_recv, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addWidget(self.recv_plot_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)

    def update_sent(self, data):
        self.l_info_sent.setText(f"Відправка: {data} МіБ")
        self.sent_data.append(data)
        if len(self.sent_data) > 80:
            self.sent_data.pop(0)
        self.sent_curve.setData(self.sent_data)

    def update_recv(self, data):
        self.l_info_recv.setText(f"Отримання: {data} МіБ")
        self.recv_data.append(data)
        if len(self.recv_data) > 80:
            self.recv_data.pop(0)
        self.recv_curve.setData(self.recv_data)

    def connects(self):
        self.btn_cpu.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_cpu))
        self.btn_memory.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_mem))
        self.btn_network.clicked.connect(lambda: self.main_window.ui.content_swidget.setCurrentWidget(self.sysmon.w_net))


class Proc(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        
        self.data_thread = DataThread()
        self.data_thread.pr_proc.connect(self.update)
        self.data_thread.start()

    def InitUI(self):
        # self.l_test = QLabel("Процеси")
        # self.v_layout = QVBoxLayout()
        # self.v_layout.addWidget(self.l_test, alignment=Qt.AlignmentFlag.AlignCenter)

        # self.setLayout(self.v_layout)
        self.Hlayout = QHBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(2)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def update(self, data):
        self.table.setRowCount(len(data)+1)
        self.table.setItem(0, 0, QTableWidgetItem("Name"))
        self.table.setItem(0, 1, QTableWidgetItem("user"))

        i = 0
        for proc in data:
            self.table.setItem(i, 0, QTableWidgetItem(proc["name"]))
            self.table.setItem(i, 1, QTableWidgetItem(proc["username"]))

            i += 1

        for i in range(self.table.columnCount()):
            self.table.resizeColumnToContents(i)


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.l_test = QLabel("Налаштування")
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.l_test, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open(style_css_path, "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()

    sys.exit(app.exec())