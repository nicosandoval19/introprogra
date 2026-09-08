# =========================
# PREGUNTA 1 — Programanjis: Detector de números peligrosos ☠️
# =========================
#
# Luego de escapar del Terraplanista, caíste en una
# nueva dimensión llena de números corruptos 😨.
#
# Los Ayudantes de Cátedra descubrieron que todos
# los números negativos son peligrosos para la estabilidad
# del universo Programanji.
#
# Recibirás una matriz representada como lista de listas.
#
# Tu misión será recorrer toda la matriz y reemplazar
# cada número negativo por el doble de su valor absoluto.
#
# Ejemplo:
#
# -3 → 6
# -8 → 16
#
# Finalmente, deberás imprimir la matriz resultante.
#
# Ejemplo 1
#
# Input:
# [[1,-2,3],[-4,5,-6]]
#
# Output:
# [[1, 4, 3], [8, 5, 12]]

matriz = eval(input())

# Tu código aquí
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if ((int(matriz[fila][columna]))<0):
            (matriz[fila][columna])=(int(matriz[fila][columna])*-2)


print(matriz    )
        
                        
                            