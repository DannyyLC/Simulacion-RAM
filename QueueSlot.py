from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets

# Representa un espacio en la cola en la interfaz gráfica
class QueueSlot(QPushButton):
    def __init__(self, process, tick_event ,parent = None,):
        super().__init__(f"Proceso {process.process_id} - {process.size*10}MB", parent)
        self.process = process # Referencia al proceso que representa
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.waiting_time = 0 # Tiempo que lleva en espera
        tick_event.connect(self.aumentarTiempo) # Conexion a funcion que aumenta el tiempo

    def aumentarTiempo(self):
        self.waiting_time += 1 # Aumentamos el tiempo que lleva en espera
        self.actualizarColor() # Actualizamos el color
    
    def actualizarColor(self):
        if self.waiting_time >= 10 and self.waiting_time < 20: # Si lleva entre 10 y 20 segundos se vuelve azul
            self.setStyleSheet("background-color: #48BCD1; color : white")
        elif self.waiting_time >= 20: # Si lleva mas de 30 segundos se vuelve morado
            self.setStyleSheet("background-color: #C55FFC ; color : white")