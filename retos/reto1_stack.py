"""
Reto 1: Validador de expresión usando Stack.
Paréntesis válidos: (), {}, []

Función a implementar:
    validate_expression(expression: str) -> bool

Reglas:
- Recorre la cadena; apila aperturas; ante un cierre, desapila y compara.
- Si al final la pila queda vacía y nunca hubo desajuste -> True.

Tips:
- Usa Stack de estructuras/stack.py
"""

from estructuras.stack import Stack

def validate_expression(expression: str) -> bool:
    pares = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = Stack()

    for char in expression:
        if char in '([{':
            stack.push(char)

        elif char in ')]}':
            if stack.is_empty():
                return False

            top = stack.pop()
            if pares[char] != top:
                return False

    # Si la pila queda vacía → está balanceado
    return stack.is_empty()

