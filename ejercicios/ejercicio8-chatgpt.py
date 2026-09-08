# =========================
# EJERCICIO 5
# =========================
# Recibirás una matriz representada como
# lista de listas.
#
# Debes reemplazar todos los números
# pares por -1.
#
# Finalmente, imprime la matriz resultante.

matriz = eval(input())

# Tu código aquí

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if ((int(matriz[fila][columna]))% 2)== 0:
            matriz[fila][columna]=-1

print(matriz)