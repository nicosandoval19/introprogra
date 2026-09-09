# ==================================================
# EJERCICIO 5
# CONTAR ELEMENTOS DE UNA LISTA
# ==================================================

"""
Haz una función recursiva llamada contar(lista)
que retorne cuántos elementos tiene la lista.

No puedes usar len().

Ejemplo:

contar([4, 7, 2, 9])

Retorna:
4
"""

def contar(lista):
    if lista==[]:
        return 0
    else:
        return 1+ contar(lista[1:])
        
    


lista = input("Ingresa números separados por espacio: ").split()

print(contar(lista))