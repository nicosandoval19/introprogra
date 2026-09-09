# ==================================================
# EJERCICIO 6
# SUMAR ELEMENTOS DE UNA LISTA
# ==================================================

"""
Haz una función recursiva llamada sumar(lista)
que retorne la suma de todos los números
de una lista.

Ejemplo:

sumar([4, 7, 2])

Retorna:
13
"""
def sumar(lista):
    if lista==[]:
        return 0
    else:
        return lista[0]+sumar(lista[1:])
        

lista = input("Ingresa números separados por espacio: ").split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

print(sumar(lista))