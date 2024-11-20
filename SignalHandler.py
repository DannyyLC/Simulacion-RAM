from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QEasingCurve, QTimer

class SignalHander:
    def __init__(self, controller, main_window) -> None:
        self.main_window = main_window # Referencia a la ventana principal
        self.controller = controller # Referencia al controlador de la aplicacion

        #Conectamos widgets con sus respectivas funciones
        self.main_window.pushButton_iniciar.clicked.connect(lambda : self.animar_boton(self.main_window.pushButton_iniciar))
        self.main_window.pushButton_detener.clicked.connect(lambda : self.animar_boton(self.main_window.pushButton_detener))
        self.main_window.pushButton_salir.clicked.connect(lambda : self.animar_boton(self.main_window.pushButton_salir))
        self.main_window.pushButton_iniciar.clicked.connect(self.iniciarSimulacion)
        self.main_window.pushButton_detener.clicked.connect(self.detenerTimer)
        self.main_window.pushButton_salir.clicked.connect(self.cerrar_ventana)
        self.main_window.comboBox_modos.currentIndexChanged.connect(self.controller.cambiarModo)
        self.controller.process_generation_controller.timer.timeout.connect(self.controller.tick_create_process)
        self.controller.time_controller.timer.timeout.connect(self.controller.tick)


    #Cambiamos la señal que ejecuta el boton verde
    def cambiarSeñalAReanudar(self):
        self.main_window.pushButton_iniciar.clicked.disconnect(self.iniciarSimulacion)

    #Animacion que muestra el boton de detener y salir una vez presionado el verde por primera vez
    def mostrar_acciones(self):
        self.main_window.ActionLayout.removeWidget(self.main_window.pushButton_iniciar)
        self.main_window.ActionLayout.removeItem(self.main_window.rightSpacer)
        self.main_window.pushButton_iniciar.hide()
        self.main_window.ActionLayout.update()
        self.main_window.pushButton_iniciar = QtWidgets.QPushButton("Reanudar")
        self.main_window.pushButton_iniciar.setObjectName("pushButton_iniciar")
        self.main_window.pushButton_iniciar.setMinimumWidth(200)
        self.main_window.ActionLayout.addWidget(self.main_window.pushButton_iniciar)
        self.main_window.pushButton_detener = QtWidgets.QPushButton("Detener")
        self.main_window.pushButton_detener.setStyleSheet("")
        self.main_window.pushButton_detener.setObjectName("pushButton_detener")
        self.main_window.pushButton_detener.setMinimumWidth(200)
        self.main_window.pushButton_salir = QtWidgets.QPushButton("Salir")
        self.main_window.pushButton_salir.setObjectName("pushButton_salir")
        self.main_window.pushButton_salir.setMinimumWidth(200)
        self.main_window.ActionLayout.addWidget(self.main_window.pushButton_detener)
        self.main_window.ActionLayout.addWidget(self.main_window.pushButton_salir)
        rightSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.main_window.ActionLayout.addItem(rightSpacer)
        self.main_window.pushButton_detener.clicked.connect(lambda : self.animar_boton(self.main_window.pushButton_detener))
        self.main_window.pushButton_salir.clicked.connect(lambda : self.animar_boton(self.main_window.pushButton_salir))
        self.main_window.pushButton_iniciar.clicked.connect(lambda : self.animar_boton(self.main_window.pushButton_iniciar))
        self.main_window.pushButton_detener.clicked.connect(self.detenerTimer)
        self.main_window.pushButton_salir.clicked.connect(self.cerrar_ventana)

    #Cierra la ventana al usar el boton de salir
    def cerrar_ventana(self):
        self.main_window.MainWindow.close()

    #Codigo que genera animacion al clickear los botones de accion
    def animar_boton(self, boton):
        # Crear la animación de expansión
        animacion_expandir = QPropertyAnimation(boton, b"geometry")
        animacion_expandir.setDuration(150)  # Duración de la animación en milisegundos
        animacion_expandir.setStartValue(boton.geometry())
        animacion_expandir.setEndValue(boton.geometry().adjusted(-4, -4, 4, 4))  # Expande el botón
        animacion_expandir.setEasingCurve(QEasingCurve.OutBounce)

        # Crear la animación de retorno al tamaño original
        animacion_reducir = QPropertyAnimation(boton, b"geometry")
        animacion_reducir.setDuration(150)
        animacion_reducir.setStartValue(boton.geometry().adjusted(-4, -4, 4, 4))
        animacion_reducir.setEndValue(boton.geometry())
        animacion_reducir.setEasingCurve(QEasingCurve.InOutQuad)

        # Crear el grupo secuencial de animaciones
        boton.animacion = QSequentialAnimationGroup()
        boton.animacion.addAnimation(animacion_expandir)
        boton.animacion.addAnimation(animacion_reducir)

        # Iniciar la animación
        boton.animacion.start()

    #Codigo que inicia la simulacion
    def iniciarSimulacion(self):
        self.cambiarSeñalAReanudar() # Cambiamos la funcion asignada al boton verde
        self.controller.time_controller.startTimer() # Iniciamos el cronometro de 1 segundo
        self.controller.process_generation_controller.startTimer() # Iniciamos el cronometro que genera procesos
        self.mostrar_acciones() # Hacemos la animacion que muestra boton de detener y de salir
        self.main_window.pushButton_iniciar.clicked.connect(self.reanudarTimer) # Conectamos el boton verde a su nueva funcion
        self.controller.slot1.fittype = self.main_window.comboBox_modos.currentIndex() + 1 # Introducimos el fittype en memoria
        self.controller.slot2.fittype = self.main_window.comboBox_modos.currentIndex() + 1   # Introducimos el fittype en memoria


    #Reanudamos los procesos
    def reanudarTimer(self):
        self.controller.queue.running = True
        self.controller.slot1.resume_ram()
        self.controller.slot2.resume_ram()
        
    #Pausamos los procesos
    def detenerTimer(self):
        self.controller.queue.running = False
        self.controller.slot1.stop_ram()
        self.controller.slot2.stop_ram()
