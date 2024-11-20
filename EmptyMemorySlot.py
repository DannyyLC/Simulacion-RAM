from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets

#Clase que representa un espacio vacio en memoria
class EmptyMemorySlot(QPushButton):
    def __init__(self, parent = None):
        super().__init__("Espacio Vacio\n10 MB", parent) # Lo inicializamos con texto
        self.setEnabled(False) # Lo desactivamos para que no pueda ser pulsado
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)