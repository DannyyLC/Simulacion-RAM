from TimeController import TimeController
from EmptyMemorySlot import EmptyMemorySlot
from ProcessSlot import ProcessSlot
from QueueSlot import QueueSlot
from Process import Process
from Queue import Queue
from SignalHandler import SignalHander
from EmptyQueueSlot import EmptyQueueSlot

class Controller:
    def __init__(self, main_window, queue, slot1, slot2, simulation_size) -> None:

        #Los argumentos para los controladores de tiempo estan en segundos
        self.time_controller = TimeController(1) #Objeto que controla el paso del tiempo para los demas widgets. Dejar en 1.
        self.process_generation_controller = TimeController(1) #Objeto que controla cada cuanto se genera un proceso.
        
        #Asigna referencias a los objetos que controla
        self.main_window = main_window
        self.queue = queue
        self.slot1 = slot1
        self.slot2 = slot2

        #Establece el tamaño de la simulacion para el controlador
        self.simulation_size = simulation_size
        self.queue_size = int(simulation_size*1.3)

        self.queue_free_slot = 0 # Inicia el indice de procesos en la cola en 0

        #Establece una referencia al controlador en los objetos que maneja
        self.queue.controller = self
        self.slot1.controller = self
        self.slot2.controller = self

        #Establece una referencia al layout donde cada instancia de memory va a insertar los procesos
        self.slot1.layout = self.main_window.Slot1Layout
        self.slot2.layout = self.main_window.Slot2Layout

        #Inicializa el tamaño disponible que aparece en el reporte de la interfaz
        espacio_disponible = self.slot1.size + self.slot2.size - self.slot1.used_space - self.slot2.used_space
        self.main_window.label_espacio_disponible.setText(f"Espacio Disponible: {espacio_disponible*10} MB")
        
        #Configuracion de la interfaz
        self.signal_handler = SignalHander(self, main_window)
        self.llenarSlots()


    #Metodo que controla el paso de un segundo en la aplicacion
    def tick(self):

        #Elige cual es la memoria con mas espacio disponible y le envia el proceso con mas prioridad en la cola
        if self.slot1.used_space <= self.slot2.used_space:
            self.queue.send_to_ram(self.slot1)
        else:
            self.queue.send_to_ram(self.slot2)
        
        #Actualiza el paso de un segundo en ambas memorias
        self.slot1.tick()
        self.slot2.tick()

        #Actualiza la informacion del reporte
        self.actualizarInfo()

    #Metodo que se utiliza para crear procesos
    def tick_create_process(self):

        # Solo genera procesos si hay espacio en la cola
        if len(self.queue.queue) < self.queue_size:
            self.queue.create_process()

    #Metodo que inicializa los slots en vacio y los configura para que se puedan estirar
    def llenarSlots(self):

        for i in range(self.simulation_size):
            self.main_window.Slot1Layout.setRowStretch(i, 1)
            self.main_window.Slot2Layout.setRowStretch(i, 1)
            self.main_window.Slot1Layout.addWidget(EmptyMemorySlot(), i, 0)
            self.main_window.Slot2Layout.addWidget(EmptyMemorySlot(), i, 0)

        for i in range(self.queue_size):
            self.main_window.QueueLayout.setRowStretch(i, 1)
            self.main_window.QueueLayout.addWidget(EmptyQueueSlot(), i, 0)


    #Metodo que remueve slots de cualquier tipo
    def removerWidgets(self, inicio, final, layout):

        for i in range(inicio, final): #Itera despejando los slots necesarios dentro del layout
            slot_to_remove = layout.itemAtPosition(i, 0).widget()
            layout.removeWidget(slot_to_remove)
            slot_to_remove.deleteLater()
        
    #Metodo que inserta espacios vacios graficamente en la memoria
    def insertarVaciosMemory(self, inicio, final, layout):

        for i in range(inicio, final):
            layout.addWidget(EmptyMemorySlot(), i, 0)

    #Metodo que inserta espacios vacios graficamente en la cola
    def insertarVaciosQueue(self, inicio, final, layout):

        for i in range(inicio, final):
            layout.addWidget(EmptyQueueSlot(), i, 0)

    #Metodo que inserta graficamente un proceso en la cola
    def insertarQueueUI(self, process):

        self.removerWidgets(self.queue_free_slot, self.queue_free_slot + 1, self.main_window.QueueLayout) #Quita los espacios vacios

        self.main_window.QueueLayout.addWidget(QueueSlot(process, self.time_controller.timer.timeout), self.queue_free_slot, 0, 1, 0) #Añade el proceso

        self.queue_free_slot += 1 #Actualiza la referencia al ultimo espacio vacio disponible

    #Metodo que inserta graficamente un proceso en la memoria
    def insertarMemoryUI(self, process, inicio, layout):
        size = process.size
        self.removerWidgets(inicio, size, layout)        

        layout.addWidget(ProcessSlot(process), inicio, 0, size, 0) #Añade el proceso        

    #Metodo que remueve procesos graficamente de la cola
    def removerQueueUI(self, process, inicio):
            slot_to_remove = self.main_window.QueueLayout.itemAtPosition(inicio, 0).widget() #Obtenemos el indice del slot a eliminar
            self.main_window.QueueLayout.removeWidget(slot_to_remove) #Eliminamos el slot

            self.move_up(inicio + 1) #Movemos los procesos restantes hacia arriba

            self.queue_free_slot -= 1 #Actualizamos la referencia al ultimo lugar vacio en la queue

            self.insertarVaciosQueue(self.queue_size - 1, self.queue_size, self.main_window.QueueLayout) #Insertamos los slots vacios

    #Metodo que remueve procesos graficamente de la memoria
    def removerMemoryUI(self, process, inicio, layout):
        slot_to_remove = layout.itemAtPosition(inicio, 0).widget()
        layout.removeWidget(slot_to_remove)

        size = process.size

        self.insertarVaciosMemory(inicio, inicio + size, layout)

    #Metodo que pausa todos los procesos
    def pausarProcesos(self):
        self.queue.stop_queue() #Pausa los procesos en cola
        self.slot1.stop_ram() #Pausa los procesos en memoria 1
        self.slot2.stop_ram() #Pausa los procesos en memoria 2

    #Metodo que reanuda la simulacion
    def reanudarSimulacion(self):
        self.queue.resume_queue() #Reanuda procesos en memoria
        self.slot1.resume_ram() #Reanuda procesos en memoria 1
        self.slot2.resume_ram() ##Reanuda procesos en memoria 2

    #Metodo que actualiza el modo de funcionamiento de las memorias
    def cambiarModo(self):

        #Actualiza el fittype de ambas memorias
        self.slot1.fittype = self.main_window.comboBox_modos.currentIndex() + 1
        self.slot2.fittype = self.main_window.comboBox_modos.currentIndex() + 1

    #Metodo que actualiza la informacion del reporte
    def actualizarInfo(self):
        espacio_disponible = self.slot1.size + self.slot2.size - self.slot1.used_space - self.slot2.used_space
        espacio_usado = self.slot1.used_space + self.slot2.used_space
        running = Process.processes_running
        paused = Process.processes_paused
        queue = len(self.queue.queue)

        self.main_window.label_espacio_disponible.setText(f"Espacio Disponible: {espacio_disponible*10} MB")
        self.main_window.label_espacio_usado.setText(f"Espacio Usado: {espacio_usado*10} MB")
        self.main_window.label_running.setText(f"Running: {running} Procesos")
        self.main_window.label_paused.setText(f"Paused: {paused} Procesos")
        self.main_window.label_queue_reporte.setText(f"Queue: {queue} Procesos")

    #Metodo que se utiliza para mover hacia arriba los procesos en la cola
    #es necesario ya que siempre queremos que aparezcan los procesos hasta arriba
    def move_up(self, inicio):
        # Mover cada botón una fila hacia arriba
        for row in range(inicio, self.main_window.QueueLayout.rowCount()):
            button = self.main_window.QueueLayout.itemAtPosition(row, 0).widget()
            if button:  # Verificar que haya un botón en esa posición
                self.main_window.QueueLayout.removeWidget(button)
                self.main_window.QueueLayout.addWidget(button, row - 1, 0)

        # Eliminar el último botón de la columna
        last_button = self.main_window.QueueLayout.itemAtPosition(self.main_window.QueueLayout.rowCount() - 1, 0)
        if last_button:
            last_button_widget = last_button.widget()
            self.main_window.QueueLayout.removeWidget(last_button_widget)
            last_button_widget.deleteLater()  # Opcional: eliminar el botón si no se reutilizará()
