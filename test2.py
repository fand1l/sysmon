from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Зміна віджетів")
        
        # Основний віджет
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Layout для основного віджету
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # Створюємо кнопки
        self.button1 = QPushButton("Показати віджет 1")
        self.button2 = QPushButton("Показати віджет 2")
        self.button3 = QPushButton("Показати віджет 3")
        self.button4 = QPushButton("Показати віджет 4")
        
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        
        # Створюємо QStackedWidget для зміни віджетів
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)
        
        # Створюємо 4 віджети
        self.widget1 = QLabel("Це віджет 1")
        self.widget2 = QLabel("Це віджет 2")
        self.widget3 = QLabel("Це віджет 3")
        self.widget4 = QLabel("Це віджет 4")
        
        # Додаємо віджети до QStackedWidget
        self.stacked_widget.addWidget(self.widget1)
        self.stacked_widget.addWidget(self.widget2)
        self.stacked_widget.addWidget(self.widget3)
        self.stacked_widget.addWidget(self.widget4)
        
        # Підключаємо кнопки до методів для зміни віджетів
        self.button1.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.widget1))
        self.button2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.widget2))
        self.button3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.widget3))
        self.button4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.widget4))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
