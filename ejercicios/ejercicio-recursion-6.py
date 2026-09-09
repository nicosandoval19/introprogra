# ==================================================
# EJERCICIO 8
# CONTAR APARICIONES
# ==================================================

"""
Haz una función recursiva llamada apariciones(lista, numero)

Debe retornar cuántas veces aparece
el número dentro de la lista.

Ejemplo:

apariciones([4,2,7,2,2,9], 2)

Retorna:
3
"""
def apariciones(lista,numero):
    if lista==[]:
        return 0
    else:
        if lista[0]==numero:
            return 1+apariciones(lista[1:],numero)
        else:
            return 0+apariciones(lista[1:],numero)

lista = input("Ingresa números separados por espacio: ").split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

numero = int(input("Número a buscar: "))

print(apariciones(lista, numero))