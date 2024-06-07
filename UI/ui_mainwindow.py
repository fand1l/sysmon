# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
import UI.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1246, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(10, 10, 191, 681))
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_menu = QLabel(self.sidebar)
        self.l_menu.setObjectName(u"l_menu")
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(12)
        font.setBold(True)
        self.l_menu.setFont(font)
        self.l_menu.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.l_menu)

        self.btn_sysinfo = QPushButton(self.sidebar)
        self.btn_sysinfo.setObjectName(u"btn_sysinfo")
        self.btn_sysinfo.setBaseSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/icons/icons/workstation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sysinfo.setIcon(icon)

        self.verticalLayout.addWidget(self.btn_sysinfo)

        self.btn_sysmon = QPushButton(self.sidebar)
        self.btn_sysmon.setObjectName(u"btn_sysmon")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/graph.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sysmon.setIcon(icon1)

        self.verticalLayout.addWidget(self.btn_sysmon)

        self.btn_proc = QPushButton(self.sidebar)
        self.btn_proc.setObjectName(u"btn_proc")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_proc.setIcon(icon2)

        self.verticalLayout.addWidget(self.btn_proc)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 506, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_settings = QPushButton(self.sidebar)
        self.btn_settings.setObjectName(u"btn_settings")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.btn_settings)

        self.btn_doc = QPushButton(self.sidebar)
        self.btn_doc.setObjectName(u"btn_doc")
        icon4 = QIcon()
        icon4.addFile("icons/doc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_doc.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.btn_doc)

        self.content_swidget = QStackedWidget(self.centralwidget)
        self.content_swidget.setObjectName(u"content_swidget")
        self.content_swidget.setGeometry(QRect(210, 10, 1021, 671))
        self.sysmon = QWidget()
        self.sysmon.setObjectName(u"sysmon")
        self.widget = QWidget(self.sysmon)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 630, 1011, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_cpu = QPushButton(self.widget)
        self.btn_cpu.setObjectName(u"btn_cpu")

        self.horizontalLayout.addWidget(self.btn_cpu)

        self.btn_mem = QPushButton(self.widget)
        self.btn_mem.setObjectName(u"btn_mem")

        self.horizontalLayout.addWidget(self.btn_mem)

        self.btn_swap = QPushButton(self.widget)
        self.btn_swap.setObjectName(u"btn_swap")

        self.horizontalLayout.addWidget(self.btn_swap)

        self.content_swidget.addWidget(self.sysmon)
        self.sysinfo = QWidget()
        self.sysinfo.setObjectName(u"sysinfo")
        self.content_swidget.addWidget(self.sysinfo)
        self.proc = QWidget()
        self.proc.setObjectName(u"proc")
        self.content_swidget.addWidget(self.proc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.content_swidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_menu.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.btn_sysinfo.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430 \u0406\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0456\u044f", None))
        self.btn_sysmon.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0438\u0439 \u041c\u043e\u043d\u0456\u0442\u043e\u0440", None))
        self.btn_proc.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u043e\u0446\u0435\u0441\u0438", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u" \u041d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.btn_doc.setText(QCoreApplication.translate("MainWindow", u" Документація", None))
        self.btn_cpu.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.btn_mem.setText(QCoreApplication.translate("MainWindow", u"Memory", None))
        self.btn_swap.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
    # retranslateUi

