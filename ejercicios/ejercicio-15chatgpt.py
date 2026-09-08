# =========================
# PREGUNTA 5 — Programanjis: El espejo dimensional 🔄
# =========================
#
# El Terraplanista activó un espejo digital
# que invierte todas las filas de la matriz 😨.
#
# Recibirás una matriz representada como lista
# de listas.
#
# Tu misión será invertir cada fila individualmente.
#
# Finalmente, imprime la matriz resultante.
#
# Ejemplo:
#
# Input:
# [[1,2,3],[4,5,6]]
#
# Output:
# [[3, 2, 1], [6, 5, 4]]

matriz = eval(input())

# Tu código aquí

for fila in range(len(matriz)):
    matriz[fila]=matriz[fila][::-1]


print(matriz)
                        
        
