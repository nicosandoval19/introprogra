# =========================
# PREGUNTA 3 — Programanjis: La diagonal sagrada ✨
# =========================
#
# Dentro de la tierra plana existe una diagonal
# sagrada que contiene energía ancestral 😳.
#
# Recibirás una matriz cuadrada representada
# como lista de listas.
#
# Tu misión será guardar todos los elementos
# de la diagonal principal en una nueva lista.
#
# Finalmente, imprime la lista resultante.
#
# Ejemplo:
#
# Input:
# [[1,2,3],[4,5,6],[7,8,9]]
#
# Output:
# [1, 5, 9]

matriz = eval(input())
lista_final=[]

# Tu código aquí
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if fila==columna:
            numero=int(matriz[fila][columna])
            lista_final.append(numero)


print(lista_final)