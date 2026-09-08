# =========================
# PREGUNTA 4 — Programanjis: Contador de enemigos 👾
# =========================
#
# Los enemigos digitales se esconden dentro
# de una matriz.
#
# Cada número par representa un enemigo activo.
#
# Recibirás una matriz representada como lista
# de listas.
#
# Tu misión será contar cuántos números pares
# existen dentro de toda la matriz.
#
# Finalmente, imprime la cantidad encontrada.
#
# Ejemplo:
#
# Input:
# [[1,2,3],[4,6,7]]
#
# Output:
# 3

matriz = eval(input())
numerosPares=0

# Tu código aquí
for fila in range(len(matriz)):
    for columna in range (len(matriz[fila])):
        if int(matriz[fila][columna])%2==0:
            numerosPares+=1

print(numerosPares)