"""Clase que define la estructura y los metodos de la cola de procesos"""
import random
from Process import Process
import Memory

class Queue:
    def __init__(self):
        self.queue = [] # Para almacenar los procesos
        self.next_process_id = 1 # ID para nuevos procesos
        self.running = True
        self.controller = None
        
    def is_empty(self):
        """Verifica si la cola esta vacia"""
        return len(self.queue) == 0
    
    def create_process(self):
    
        if self.running:
            """Crea un nuevo proceso con tamaño y duracion aleatorios"""
            size = random.randint(1, 3) # Tamaño en MB
            duration = random.randint(10, 20) # Duracion en segundos
            
            # Creacion de el proceso
            process = Process(self.next_process_id, size, duration)
            self.next_process_id += 1
            
            # Añadir proceso al final de la cola
            self.queue.append(process)
            self.controller.insertarQueueUI(process)
            return self.next_process_id
        
    def send_to_ram(self, ram):
        """Elimina el primer proceso de la cola que cabe en la RAM, si existe y lo retorna"""
        if self.running:
            if self.is_empty():
                return None
            
            # Extraer el primer proceso de la cola
            for i, process in enumerate(self.queue):
                if ram.fit(process): # Se verifica si hay espacio suficiente en la ram para el proceso
                    self.controller.removerQueueUI(process, i)
                    process.on_terminate = ram.remove_Process #Le damos a process la referencia al metodo de remove_Proces de la ram que lo almacena
                    process.is_running = True #Iniciamos el proceso como running
                    return self.queue.pop(i) # Si hay espacio suficiente remueve el proceso de la cola y lo retorna
            return None

    def stop_process(self, process_id):
        """Detiene un proceso en la cola"""
        for process in self.queue:
            if process.process_id == process_id:
                process.stop()
                return True
        return False
    
    def resume_process(self, process_id):
        """Reanuda un proceso en la cola"""
        for process in self.queue:
            if process.process_id == process_id:
                process.resume()
                return True
        return False

    def stop_queue(self):
        """Detiene la creacion de procesos en el queue"""
        self.running = False
    
    def resume_queue(self):
        """Reanuda la creacion de procesos en el queue"""
        self.running = True
                
            
        
        