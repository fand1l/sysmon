import sys
from PySide6.QtWidgets import (
            QApplication, QMainWindow, QWidget,
            QLabel, QVBoxLayout
            )
from PySide6.QtCore import QFile, QThread, Signal, Qt
from UI.ui_mainwindow import Ui_MainWindow

import init.os_info
import init.proc
import init.sysmon


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

    def run(self):
        while True:
            os_i = init.os_info.os_init()
            os_system = init.os_info.os_system
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
                    self.os_uptime.emit(f"Час роботи: {os_i[9]}")
                
                elif os_system == "Windows":
                    self.os_ready.emit(f"Вітаю, {os_i[9]}! Ваша операційна система {os_i[0]} {os_i[1]} частково підтримується!")
                
            else:
                self.os_ready.emit(f"Нажаль ваша операційна система не підтримується")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect()

        self.w_os_ready = OS_Ready()
        self.w_os_info = OS_Info()
        self.w_sysmon = System_Monitor()
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
        self.l_ready_os = QLabel("Завантаження данних про операційну систему!\n Якщо завантаження йде занадто довго:\nLinux Based OS: Запустіть програму з правами рута: sudo, su або doas\nMSDOS/Windows Based OS: запустіть програму з правами адміністратра: ПКМ >> Виконати з правами Адміністратора")
        self.v_layout = QVBoxLayout()
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

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.l_name)
        self.v_layout.addWidget(self.l_release)
        self.v_layout.addWidget(self.l_dewm)
        self.v_layout.addWidget(self.l_user)
        self.v_layout.addWidget(self.l_host)
        self.v_layout.addWidget(self.l_cpu)
        self.v_layout.addWidget(self.l_arch)
        self.v_layout.addWidget(self.l_memory)
        self.v_layout.addWidget(self.l_swap)
        self.v_layout.addWidget(self.l_partitions)
        self.v_layout.addWidget(self.l_uptime)

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
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.l_test = QLabel("Системний монітор")
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.l_test, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)


class Proc(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.l_test = QLabel("Процеси")
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.l_test, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.v_layout)


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

    window = MainWindow()
    window.show()

    sys.exit(app.exec())