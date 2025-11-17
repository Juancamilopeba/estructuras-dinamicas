"""
Reto 3: Gestor de tareas con DoublyLinkedList.

Funciones a implementar (usa DoublyLinkedList de estructuras/linkedlist.py):
    - add_task(id:int, descripcion:str, prioridad:int) -> None
    - find_by_id(id:int) -> dict|None
    - find_by_priority(prioridad:int) -> list[dict]

Nota:
- La lista interna debe almacenar dicts con llaves: id, descripcion, prioridad.
"""

from estructuras.linkedlist import DoublyLinkedList

class TaskManager:
    def __init__(self):
        self.tasks = DoublyLinkedList()

    def add_task(self, task_id: int, nombre: str, prioridad: int):
        """
        Agrega una tarea usando append.
        Cada tarea es un diccionario.
        """
        task = {
            "id": task_id,
            "nombre": nombre,
            "prioridad": prioridad
        }
        self.tasks.append(task)

    def find_by_id(self, task_id: int):
        """
        Busca una tarea por ID usando la DLL.
        Retorna dict o None.
        """
        return self.tasks.find_by_id(task_id)

    def find_by_priority(self, prioridad: int):
        """
        Busca todas las tareas con esa prioridad.
        Retorna lista de dicts.
        """
        return self.tasks.find_by_prioridad(prioridad)

