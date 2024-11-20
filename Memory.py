import random
import Process

class Memory:
    def __init__(self, size):
        self.slots = [None] * size # Lista con los procesos en el slot
        self.used_space = 0 # Espacio utilizado
        self.size = size # Tamaño de el slot en MB
        self.fittype = 1
        self.controller = None
        self.layout = None # Referencia al layout que representa su memoria en la UI
        
    def first_fit(self, process):
        """Encuentra el primer bloque contiguo que pueda acomodar el proceso y lo asigna."""
        current_start = None  # Inicio del bloque actual
        current_block_size = 0  # Tamaño del bloque actual

        for i in range(self.size):
            if self.slots[i] is None:
                # Si encontramos una posición vacía, empezamos o continuamos un bloque
                if current_start is None:
                    current_start = i
                current_block_size += 1

                # Verifica si el bloque es suficiente para el proceso
                if current_block_size == process.size:
                    # Asigna el proceso al primer bloque adecuado
                    for j in range(current_start, current_start + process.size):
                        self.slots[j] = process
                    self.used_space += process.size
                    self.controller.insertarMemoryUI(process, current_start, self.layout)
                    return True  # Proceso colocado exitosamente
                
            else:
                # Reinicia el bloque cuando se encuentra un espacio ocupado
                current_start = None
                current_block_size = 0

        # No se encontró un bloque adecuado
        return False
    
    def best_fit(self, process):
        """Encuentra el bloque contiguo más pequeño que pueda acomodar el proceso y lo asigna."""
        best_start = -1
        min_block_size = self.size + 1  # Un valor mayor que el tamaño total de memoria
        current_start = None
        current_block_size = 0

        for i in range(self.size):
            if self.slots[i] is None:
                # Inicio de un nuevo bloque vacío
                if current_start is None:
                    current_start = i
                current_block_size += 1

                if i == self.size - 1 and current_block_size >= process.size and current_block_size < min_block_size:
                        best_start = current_start
                        min_block_size = current_block_size

            else:
                # Si el bloque encontrado es el mejor hasta ahora y lo suficientemente grande
                if current_block_size >= process.size and current_block_size < min_block_size:
                    best_start = current_start
                    min_block_size = current_block_size

                # Reinicia el bloque cuando se encuentra un espacio ocupado
                current_start = None
                current_block_size = 0

        # Si encontramos un bloque adecuado
        if best_start != -1:
            for i in range(best_start, best_start + process.size):
                self.slots[i] = process  # Asigna el proceso a cada unidad de espacio en el bloque
            self.used_space += process.size
            self.controller.insertarMemoryUI(process, best_start, self.layout)
            return True  # Proceso colocado exitosamente

        return False  # No hay espacio contiguo suficiente para el proceso
    
    def worst_fit(self, process):
        """Encuentra el bloque más grande que pueda acomodar el proceso y lo asigna."""
        largest_start = None  # Índice inicial del bloque más grande encontrado
        largest_block_size = 0  # Tamaño del bloque más grande encontrado
        current_start = None  # Inicio del bloque actual
        current_block_size = 0  # Tamaño del bloque actual

        # Recorrer toda la memoria para encontrar el bloque más grande disponible
        for i in range(self.size):
            if self.slots[i] is None:
                # Encontramos una posición vacía, aumentamos el bloque actual
                if current_start is None:
                    current_start = i
                current_block_size += 1
            else:
                # Si el bloque actual es el más grande hasta ahora, lo guardamos
                if current_block_size > largest_block_size:
                    largest_block_size = current_block_size
                    largest_start = current_start
                # Reiniciamos el bloque al encontrar un espacio ocupado
                current_start = None
                current_block_size = 0

        # Después del bucle, revisamos el último bloque contiguo
        if current_block_size > largest_block_size:
            largest_block_size = current_block_size
            largest_start = current_start

        # Verificamos si encontramos un bloque lo suficientemente grande
        if largest_block_size >= process.size:
            # Asignamos el proceso al bloque más grande encontrado
            for j in range(largest_start, largest_start + process.size):
                self.slots[j] = process
            self.used_space += process.size
            self.controller.insertarMemoryUI(process, largest_start, self.layout)
            return True  # Proceso colocado exitosamente

        # No se encontró un bloque adecuado
        return False
   
    def fit(self, process):
        """Determina donde se puede colocar el proceso usando la estrategia seleccionada"""
        flag = False

        if self.fittype == 1:
            flag = self.first_fit(process)
        elif self.fittype == 2:
            flag = self.best_fit(process)
        else:
            flag = self.worst_fit(process)
            
        return flag     
    
    def stop_ram(self):
        """Detiene todos los procesos que se estan ejecutando en la RAM"""
        for i in range(self.size):
            if self.slots[i] is not None:
                self.slots[i].stop() # Detenemos el proceso
    
    def resume_ram(self):
        """Reanuda todos los procesos en la RAM"""
        for i in range(self.size):
            if self.slots[i] is not None:
                self.slots[i].resume()  # Reanudamos el proceso
                
    def stop_process(self, process_id):
        """Detiene un proceso en la memoria."""
        self.slot[process_id].stop()

    def resume_process(self, process_id):
        """Reanuda un proceso en la memoria."""
        self.slot[process_id].resume()
    
    def remove_Process(self, process_id):
        """Elimina lógicamente un proceso de la memoria liberando su espacio."""
        removed = False
        for i in range(self.size):
            # Verifica si la posición tiene un proceso y coincide con el ID
            if self.slots[i] is not None and self.slots[i].process_id == process_id:
                process = self.slots[i]
                inicio = i - process.size + 1
                self.slots[i] = None  # Liberar la posición
                removed = True
                self.used_space -= 1  # Reducimos el espacio utilizado en la RAM

        self.controller.removerMemoryUI(process, inicio, self.layout)

        return removed
    
    def tick(self):
        prev_process = None
        current_process = None

        for process in self.slots:
            current_process = process

            if process is not None and (current_process != prev_process):
                process.tick()

            prev_process = process

    def iniciar(self, process_id):
        """Inicializa la ram con procesos aleatorios"""

            
