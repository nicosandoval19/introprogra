# ==================================================
# EJERCICIO 1
# CONTAR HACIA ATRÁS
# ==================================================

"""
Crea una función recursiva que reciba un número n
y muestre todos los números desde n hasta 0.

Ejemplo:
5
4
3
2
1
0
"""

def contar(n):
    if n==0:
        print(0)
    else:
        
         
        return contar(n-1)
        

n = int(input("Ingresa un número: "))

(contar(n))