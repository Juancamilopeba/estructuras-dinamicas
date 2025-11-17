"""
Lista doblemente enlazada (DLL) para gestionar tareas.

TODO:
- Implementa DoubleNode (id, descripcion, prioridad, prev, next)
- Implementa DoublyLinkedList con: append, prepend, remove_by_id, find_by_id, find_by_prioridad, iter_forward, iter_backward, size
- Mantén head, tail y contador para O(1) en inserciones a extremos.

Nota:
- 'find' será O(n) lineal.
"""

class DoubleNode:
    def __init__(self, task):
        self.task = task        # task es un diccionario con {id, nombre, prioridad}
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, task):
        """Inserta al final. O(1)"""
        node = DoubleNode(task)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1

    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        node = DoubleNode(task)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        current = self.head

        while current:
            if current.task["id"] == task_id:

                # caso: único nodo
                if current is self.head and current is self.tail:
                    self.head = self.tail = None

                # caso: es cabeza
                elif current is self.head:
                    self.head = current.next
                    self.head.prev = None

                # caso: es cola
                elif current is self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # caso: nodo intermedio
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self._size -= 1
                return True

            current = current.next

        return False

    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        current = self.head
        while current:
            if current.task["id"] == task_id:
                return current.task
            current = current.next
        return None

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        results = []
        current = self.head
        while current:
            if current.task["prioridad"] == prioridad:
                results.append(current.task)
            current = current.next
        return results

    def iter_forward(self):
        """Generador hacia adelante."""
        current = self.head
        while current:
            yield current.task
            current = current.next

    def iter_backward(self):
        """Generador hacia atrás."""
        current = self.tail
        while current:
            yield current.task
            current = current.prev

    def size(self):
        """Cantidad de nodos. O(1)"""
        return self._size

