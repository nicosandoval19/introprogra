# =========================
# PREGUNTA 2 — Programanjis: Los números impares atacan 😡
# =========================
#
# El Terraplanista liberó una ola de números impares
# dentro de la máquina virtual.
#
# Para detenerlos, deberás recorrer una matriz y
# reemplazar todos los números impares por 0.
#
# Los números pares deben mantenerse iguales.
#
# Finalmente, imprime la matriz resultante.
#
# Ejemplo:
#
# Input:
# [[1,2,3],[4,5,6]]
#
# Output:
# [[0, 2, 0], [4, 0, 6]]

matriz = eval(input())

# Tu código aquí
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if (int(matriz[fila][columna])%2)!=0:
           (matriz[fila][columna])=0
        
print(matriz)