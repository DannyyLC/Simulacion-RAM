from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets

# Clase que crea un espacio vacio en la cola
class EmptyQueueSlot(QPushButton):
    def __init__(self, parent = None):
        super().__init__("Espacio Vacio", parent) # Texto que aparece en el boton
        self.setEnabled(False) # Lo desactivamos porque no queremos que sea pulsado
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)