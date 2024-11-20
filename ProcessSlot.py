from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5 import QtWidgets

# Clase que genera el proceso en la interfaz gráfica
class ProcessSlot(QPushButton):
    def __init__(self, process, parent=None):
        super().__init__(parent)
        self.process = process # Proceso asignado al boton 
        self.process_id = process.process_id # ID del proceso
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.clicked.connect(self.press_button) # Conexion cada vez que se clikea el boton

        self.process.tiempo_cambiado.connect(self.actualizar_texto) # Actualizamos el texto cada que pasa un segundo
        self.process.state_changed.connect(self.runningChanged) # Actualizamos el color del boton dependiendo de su estado
        self.actualizar_texto(self.process.remaining_time) # Inicializamos el tiempo
    
    def actualizar_texto(self, remaining_time):
        self.setText(f"Proceso {self.process_id} - Tiempo Restante: {remaining_time}s\n{self.process.size*10} MB") # Ajustamos el tiempo

    def runningChanged(self):
        if self.process.is_running: # El proceso esta corriendo
            self.setStyleSheet("background-color:red; color : white") 
        else: # El proceso esta pausado
            self.setStyleSheet("background-color:yellow; color : black")

    # Funcion que se llama al presionar el boton
    def press_button(self):
        if self.process.is_running:
            self.process.is_runing = False # Si el proceso estaba corriendo lo detenemos
            self.process.stop()
            self.setStyleSheet("background-color:yellow; color : black") # Actualizamos su color
        else:
            self.process.is_runing = True # Reanudamos el proceso
            self.process.resume()
            self.setStyleSheet("background-color:red; color : white") # Actualizamos su color
            