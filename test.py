import sys
import psutil
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PySide6.QtCore import QTimer, QThread, Signal
import pyqtgraph as pg

class DataThread(QThread):
    data_updated = Signal(float, float)  # Сигнал для передачі даних CPU та оперативної пам'яті

    def run(self):
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent
            self.data_updated.emit(cpu_usage, memory_usage)  # Передача даних через сигнал

class SystemMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Monitor")
        self.resize(800, 300)  # Встановлення розміру вікна

        # Головний віджет і макет
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Написи для відображення використання CPU і оперативної пам'яті
        self.cpu_label = QLabel("CPU Usage: 0%")
        self.memory_label = QLabel("Memory Usage: 0%")
        main_layout.addWidget(self.cpu_label)
        main_layout.addWidget(self.memory_label)

        # Макет для графіків
        graph_layout = QHBoxLayout()
        main_layout.addLayout(graph_layout)

        # Створення графіка для CPU
        self.cpu_plot_widget = pg.PlotWidget()
        graph_layout.addWidget(self.cpu_plot_widget)

        # Налаштування графіка для CPU
        self.cpu_plot_widget.setYRange(0, 100)
        self.cpu_plot_widget.setLabel('left', 'CPU Usage (%)')
        self.cpu_plot_widget.setLabel('bottom', 'Time (s)')
        self.cpu_plot_widget.setFixedHeight(150)  # Встановлення висоти графіка

        # Дані для графіка CPU
        self.cpu_data = []
        self.cpu_curve = self.cpu_plot_widget.plot(self.cpu_data, pen='g')

        # Створення графіка для оперативної пам'яті
        self.memory_plot_widget = pg.PlotWidget()
        graph_layout.addWidget(self.memory_plot_widget)

        # Налаштування графіка для оперативної пам'яті
        self.memory_plot_widget.setYRange(0, 100)
        self.memory_plot_widget.setLabel('left', 'Memory Usage (%)')
        self.memory_plot_widget.setLabel('bottom', 'Time (s)')
        self.memory_plot_widget.setFixedHeight(150)  # Встановлення висоти графіка

        # Дані для графіка оперативної пам'яті
        self.memory_data = []
        self.memory_curve = self.memory_plot_widget.plot(self.memory_data, pen='b')

        # Створення потоку для отримання даних
        self.data_thread = DataThread()
        self.data_thread.data_updated.connect(self.update_data)
        self.data_thread.start()

    def update_data(self, cpu_usage, memory_usage):
        # Оновлення даних графіка CPU
        self.cpu_data.append(cpu_usage)
        if len(self.cpu_data) > 60:  # показуємо останні 60 значень
            self.cpu_data.pop(0)
        self.cpu_curve.setData(self.cpu_data)

        # Оновлення напису для CPU
        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")

        # Оновлення даних графіка оперативної пам'яті
        self.memory_data.append(memory_usage)
        if len(self.memory_data) > 60:  # показуємо останні 60 значень
            self.memory_data.pop(0)
        self.memory_curve.setData(self.memory_data)

        # Оновлення напису для оперативної пам'яті
        self.memory_label.setText(f"Memory Usage: {memory_usage}%")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SystemMonitor()
    window.show()
    sys.exit(app.exec())
