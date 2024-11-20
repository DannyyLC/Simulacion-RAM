import sys
from load_styles import load_stylesheets
from Controller import Controller
from Queue import Queue
from Memory import Memory
from PyQt5 import QtWidgets
from Ui_MainWindow import Ui_MainWindow

if __name__ == "__main__":
    simulation_size = 16 #Selecciona el numero de slots en memoria. El numero de Slots en Queue sera 1.3 este valor.

    app = QtWidgets.QApplication(sys.argv) #Crea una instancia de una app de PyQt5
    stylesheet = load_stylesheets("main_window.qss", "lines.qss", "labels.qss","container.qss","combobox.qss","buttons.qss") #Importa estilos
    app.setStyleSheet(stylesheet) #Aplica los estilos
    MainWindow = QtWidgets.QMainWindow() #Crea la ventana principal
    ui = Ui_MainWindow(MainWindow) #Crea una instancia de nuestra clase de interfaz grafica y la configura
    queue = Queue() #Crea una instancia de la Queue
    slot1 = Memory(simulation_size) #Crea la instancia que manejará el primer slot de memoria
    slot2 = Memory(simulation_size) #Crea la instancia que manejará el segundo slot de memoria
    controller = Controller(ui, queue, slot1, slot2, simulation_size) #Crea una instancia del controlador que conecta la logica y la interfaz
    MainWindow.showMaximized() #Maximiza la ventana
    sys.exit(app.exec_())
