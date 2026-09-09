# ==================================================
# EJERCICIO 2
# SUMAR HASTA N
# ==================================================

"""
Haz una función recursiva llamada suma_hasta(n)
que retorne la suma de todos los números desde
1 hasta n.

Ejemplo:
suma_hasta(4)

Retorna:
10
"""

def suma_hasta(n):
    if n==0:
        return 0
    else:
        #n+suma_hasta(n-1)
        #
        return(n+suma_hasta(n-1))


n = int(input("Ingresa un número: "))

print(suma_hasta(n))