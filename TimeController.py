from PyQt5.QtCore import QTimer

#Clase que controla el paso del tiempo
class TimeController:
    def __init__(self, time) -> None:
        self.time = time*1000 #Multiplicamos time por 1000 ya que el timer utiliza milisegundos como argumento
        self.timer = QTimer() #Crea una instancia de QTimer. QTimer es un cronometro de la clase PyQt5
    
    def startTimer(self):
        self.timer.start(self.time) #Iniciamos el cronometro pasando el tiempo en milimetros. Cada que pase el tiempo indicado
                                    #se va a emitir una señal
    