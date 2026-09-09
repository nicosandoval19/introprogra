# ==================================================
# EJERCICIO 3
# FACTORIAL
# ==================================================

"""
Haz una función recursiva llamada factorial(n)
que calcule el factorial de n.

Ejemplo:
factorial(5)

Retorna:
120
"""


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Ingresa un número: "))

print(factorial(n))