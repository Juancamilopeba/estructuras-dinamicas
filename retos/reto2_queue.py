"""
Reto 2: Simulador de atención usando Queue (FIFO).

Clase a implementar:
    class QueueManager:
        - add_person(nombre: str, tiempo: int) -> None
        - serve_person() -> tuple[str, int]   # (nombre, tiempo)
        - state() -> list[str]                # nombres en orden FIFO

Reglas:
- 'agregar_persona' encola al final.
- 'atender_persona' desencola y retorna la tupla; si está vacía, lanza IndexError.
- 'estado' retorna los nombres en el orden actual sin mutar la cola.

Tips:
- Usa Queue de estructuras/queue.py
"""

from estructuras.queue import Queue

class QueueManager:
    def __init__(self):
        self.queue = Queue()

    def add_person(self, nombre: str, tiempo: int):
        """
        Agrega una persona a la cola.
        value almacenado: (nombre, tiempo)
        """
        self.queue.enqueue((nombre, tiempo))

    def serve_person(self):
        """
        Atiende al primero en la cola.
        Retorna (nombre, tiempo) o None si la cola está vacía.
        """
        if self.queue.is_empty():
            return None
        return self.queue.dequeue()

    def state(self):
        """
        Retorna una lista de strings para mostrar el estado.
        Ejemplo: ["Juan - 5", "Ana - 3"]
        """
        estado = []
        current = self.queue.head

        while current:
            nombre, tiempo = current.value
            estado.append(f"{nombre} - {tiempo}")
            current = current.next

        return estado
