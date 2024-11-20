from PyQt5.QtCore import QObject, pyqtSignal

class Process(QObject):
    tiempo_cambiado = pyqtSignal(int)  # Señal que emite el tiempo restante
    state_changed = pyqtSignal()       # Señal que indica cambio de estado

    processes_running = 0
    processes_paused = 0

    def __init__(self, process_id, size, duration):
        super().__init__()
        self.process_id = process_id      # ID único del proceso
        self.size = size                  # Tamaño en MB
        self.duration = duration          # Duración en segundos
        self._is_running = False          # Estado del proceso
        Process.processes_paused += 1     # Incrementamos el numero de procesos pausados
        self._remaining_time = duration   # Tiempo restante del proceso
        self.on_terminate = None          # Referencia al metodo de la RAM que lo va a eliminar
    
    @property # Definimos una propiedad para el atributo is_running, la usaremos para generar señales cuando cambie su estado
    def is_running(self):
        return self._is_running

    @is_running.setter # Al llamar el setter de la propiedad se ejecuta el siguiente codigo
    def is_running(self, state):
        if self._is_running != state:     # Verificamos que exista un cambio de estado entre paused y running
            self._is_running = state     # Hacemos el cambio de estado
            self.state_changed.emit()    # Emitimos señal de que el estado ha cambiado

        if state:
            Process.processes_running += 1 #Si el proceso cambia a running incrementamos el numero de procesos corriendo
            Process.processes_paused -= 1 #Si el proceso cambia a running decrementamos el numero de procesos pausados
        else:
            Process.processes_running -= 1 #Si el proceso cambia a paused decrementamos el numero de procesos corriendo
            Process.processes_paused += 1 #Si el proceso cambia a paused incrementamos el numero de procesos pausados

    @property #Propiedad del atributo remaining_time
    def remaining_time(self):
        return self._remaining_time

    @remaining_time.setter #Al llamar el metodo set de remaining_time se ejecuta este codigo
    def remaining_time(self, nuevo_tiempo):
        if nuevo_tiempo != self._remaining_time: # Verificamos que exista un cambio en el tiempo restante del proceso
            self._remaining_time = nuevo_tiempo # Asignamos el nuevo tiempo al proceso
            self.tiempo_cambiado.emit(self._remaining_time)  # Emitir señal cuando cambia el tiempo

    def stop(self):
        """Detiene el proceso."""
        if self.is_running:
            self.is_running = False
    
    def resume(self):
        """Reanuda el proceso."""
        if not self.is_running:
            self.is_running = True

    def terminate(self):
        """Elimina el proceso."""
        self.on_terminate(self.process_id)
        Process.processes_running -= 1
            
    def tick(self):
        """Simula el paso del tiempo en el proceso."""
        if self.is_running and self.remaining_time > 0:
            self.remaining_time -= 1
        
        if self.remaining_time == 0:
                self.terminate()
