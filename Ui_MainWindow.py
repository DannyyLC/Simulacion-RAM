from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QEasingCurve, QTimer

class Ui_MainWindow(object):
    def __init__(self, MainWindow) -> None:
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        #Configura la interfaz grafica. Codigo generado con QtDesigner
        
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 538)
        MainWindow.setStyleSheet("")
        self.isStarted = False
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QGridLayout()
        self.MainLayout.setContentsMargins(30, -1, 90, -1)
        self.MainLayout.setObjectName("MainLayout")
        self.ProcessSlotLayout = QtWidgets.QGridLayout()
        self.ProcessSlotLayout.setContentsMargins(20, 15, -1, -1)
        self.ProcessSlotLayout.setObjectName("ProcessSlotLayout")
        self.QueueLayout = QtWidgets.QGridLayout()
        self.QueueLayout.setObjectName("QueueLayout")
        self.ProcessSlotLayout.addLayout(self.QueueLayout, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ProcessSlotLayout.addWidget(self.line_3, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(150)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.ProcessSlotLayout.addWidget(self.line, 1, 0, 1, 1)
        self.Slot1Layout = QtWidgets.QGridLayout()
        self.Slot1Layout.setObjectName("Slot1Layout")
        self.ProcessSlotLayout.addLayout(self.Slot1Layout, 2, 2, 1, 1)
        self.Slot2Layout = QtWidgets.QGridLayout()
        self.Slot2Layout.setObjectName("Slot2Layout")
        self.ProcessSlotLayout.addLayout(self.Slot2Layout, 2, 4, 1, 1)
        self.label_queue_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_queue_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_queue_titulo.setObjectName("label_queue_titulo")
        self.ProcessSlotLayout.addWidget(self.label_queue_titulo, 0, 0, 1, 1)
        self.label_slot1 = QtWidgets.QLabel(self.centralwidget)
        self.label_slot1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot1.setObjectName("label_slot1")
        self.ProcessSlotLayout.addWidget(self.label_slot1, 0, 2, 1, 1)
        self.label_slot2 = QtWidgets.QLabel(self.centralwidget)
        self.label_slot2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_slot2.setObjectName("label_slot2")
        self.ProcessSlotLayout.addWidget(self.label_slot2, 0, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.line_2.setMinimumSize(QtCore.QSize(75, 0))
        self.line_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ProcessSlotLayout.addWidget(self.line_2, 1, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.ProcessSlotLayout.addWidget(self.line_5, 1, 4, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setMaximumSize(QtCore.QSize(25, 16777215))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.ProcessSlotLayout.addWidget(self.line_4, 1, 3, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.ProcessSlotLayout.addWidget(self.line_6, 3, 0, 1, 5)
        self.MainLayout.addLayout(self.ProcessSlotLayout, 1, 1, 1, 1)
        self.ActionLayout = QtWidgets.QHBoxLayout()
        self.ActionLayout.setContentsMargins(-1, 45, -1, -1)
        self.ActionLayout.setSpacing(20)
        self.ActionLayout.setObjectName("ActionLayout")
        self.ActionLayout.setAlignment(Qt.AlignCenter)
        leftSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ActionLayout.insertItem(0, leftSpacer)
        self.label_acciones = QtWidgets.QLabel(self.centralwidget)
        self.label_acciones.setAlignment(QtCore.Qt.AlignRight)
        self.label_acciones.setObjectName("label_acciones")
        self.ActionLayout.addWidget(self.label_acciones)
        self.pushButton_iniciar = QtWidgets.QPushButton()
        self.pushButton_iniciar.setObjectName("pushButton_iniciar")
        self.pushButton_iniciar.setMinimumWidth(200)
        self.ActionLayout.addWidget(self.pushButton_iniciar)
        self.pushButton_detener = QtWidgets.QPushButton()
        self.pushButton_salir = QtWidgets.QPushButton()
        self.rightSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ActionLayout.addItem(self.rightSpacer)
        self.MainLayout.addLayout(self.ActionLayout, 0, 1, 1, 1)
        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.LeftLayout.setContentsMargins(-1, 10, 15, -1)
        self.LeftLayout.setObjectName("LeftLayout")
        spacer1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.LeftLayout.addItem(spacer1)
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.label_titulo.setMaximumWidth(600)
        self.LeftLayout.addWidget(self.label_titulo)
        spacer2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.LeftLayout.addItem(spacer2)
        self.ModeLayout = QtWidgets.QHBoxLayout()
        self.ModeLayout.setObjectName("ModeLayout")
        self.label_modo = QtWidgets.QLabel(self.centralwidget)
        self.label_modo.setStyleSheet("")
        self.label_modo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modo.setObjectName("label_modo")
        self.ModeLayout.addWidget(self.label_modo)
        self.comboBox_modos = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_modos.setObjectName("comboBox_modos")
        self.comboBox_modos.addItems(["Primer", "Mejor", "Peor"])
        self.ModeLayout.addWidget(self.comboBox_modos)
        self.LeftLayout.addLayout(self.ModeLayout)
        spacer3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.LeftLayout.addItem(spacer3)

        self.contenedor = QWidget()
        self.contenedor.setObjectName("contenedor")

        self.ReporteLayout = QtWidgets.QVBoxLayout()
        self.ReporteLayout.setObjectName("ReporteLayout")
        self.label_titulo_reporte = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo_reporte.setStyleSheet("")
        self.label_titulo_reporte.setAlignment(QtCore.Qt.AlignLeft)
        self.label_titulo_reporte.setObjectName("label_titulo_reporte")
        self.ReporteLayout.addWidget(self.label_titulo_reporte)
        self.label_espacio_disponible = QtWidgets.QLabel(self.centralwidget)
        self.label_espacio_disponible.setAlignment(QtCore.Qt.AlignLeft)
        self.label_espacio_disponible.setObjectName("label_espacio_disponible")
        self.ReporteLayout.addWidget(self.label_espacio_disponible)
        self.label_espacio_usado = QtWidgets.QLabel(self.centralwidget)
        self.label_espacio_usado.setAlignment(QtCore.Qt.AlignLeft)
        self.label_espacio_usado.setObjectName("label_espacio_usado")
        self.ReporteLayout.addWidget(self.label_espacio_usado)
        self.label_running = QtWidgets.QLabel(self.centralwidget)
        self.label_running.setAlignment(QtCore.Qt.AlignLeft)
        self.label_running.setObjectName("label_running")
        self.ReporteLayout.addWidget(self.label_running)
        self.label_paused = QtWidgets.QLabel(self.centralwidget)
        self.label_paused.setAlignment(QtCore.Qt.AlignLeft)
        self.label_paused.setObjectName("label_paused")
        self.ReporteLayout.addWidget(self.label_paused)
        self.label_queue_reporte = QtWidgets.QLabel(self.centralwidget)
        self.label_queue_reporte.setAlignment(QtCore.Qt.AlignLeft)
        self.label_queue_reporte.setObjectName("label_queue_reporte")
        self.ReporteLayout.addWidget(self.label_queue_reporte)
        self.ReporteLayout.setSpacing(20)
        self.Slot1Layout.setSpacing(0)  # Elimina el espacio entre widgets
        self.Slot2Layout.setSpacing(0)
        self.QueueLayout.setSpacing(0)
        self.contenedor.setLayout(self.ReporteLayout)

        self.LeftLayout.addWidget(self.contenedor)
        spacer4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.LeftLayout.addItem(spacer4)
        self.MainLayout.addLayout(self.LeftLayout, 0, 0, 2, 1)
        self.MainLayout.setColumnMinimumWidth(0, 1)
        self.MainLayout.setColumnMinimumWidth(1, 2)
        self.MainLayout.setColumnStretch(1, 1)
        self.MainLayout.setRowStretch(1, 1)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulacion de memoria"))
        self.label_queue_titulo.setText(_translate("MainWindow", "QUEUE"))
        self.label_slot1.setText(_translate("MainWindow", "SLOT 1"))
        self.label_slot2.setText(_translate("MainWindow", "SLOT 2"))
        self.label_acciones.setText(_translate("MainWindow", "Acciones:"))
        self.pushButton_iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.pushButton_detener.setText(_translate("MainWindow", "Detener"))
        self.pushButton_salir.setText(_translate("MainWindow", "Salir"))
        self.label_titulo.setText(_translate("MainWindow", "SIMULACIÓN\nDE MEMORIA"))
        self.label_modo.setText(_translate("MainWindow", "Modo:"))
        self.label_titulo_reporte.setText(_translate("MainWindow", "Reporte de Uso"))
        self.label_running.setText(_translate("MainWindow", "Running: 0 Procesos"))
        self.label_paused.setText(_translate("MainWindow", "Paused: 0 Procesos"))
        self.label_queue_reporte.setText(_translate("MainWindow", "Queue: 0 Procesos"))
        self.label_espacio_usado.setText(_translate("MainWindow", "Espacio Usado: 0 MB"))
        self.label_espacio_disponible.setText(_translate("MainWindow", "Espacio Disponible: 24 MB"))
        self.comboBox_modos.changeEvent
