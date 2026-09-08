# =========================
# EJERCICIO 6
# =========================
# Recibirás una matriz representada como
# lista de listas.
#
# Debes contar cuántos números pares
# existen en toda la matriz.
#
# Finalmente, imprime la cantidad.

matriz = eval(input())
pares=0

# Tu código aquí

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if ((int(matriz[fila][columna])) %2)==0:
            pares+=1



print(pares)