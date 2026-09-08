# =========================
# PREGUNTA 6 — Programanjis: Detector de primos ☢️
# =========================
#
# Los Ayudantes descubrieron que los números
# primos generan inestabilidad dimensional 😭.
#
# Recibirás una matriz representada como lista
# de listas.
#
# Cada vez que exista un número primo,
# deberá ser reemplazado por el doble
# de su valor.
#
# Finalmente, imprime la matriz resultante.
#
# Hint:
# Se recomienda crear una función:
#
# def es_primo(numero):
#
# Ejemplo:
#
# Input:
# [[2,4,5],[6,7,8]]
#
# Output:
# [[4, 4, 10], [6, 14, 8]]

matriz = eval(input())


# Tu código aquí

def es_primo(numero):
    for divisor in range(2,numero):
        if numero%divisor==0:
            return False
        
            
        
    return True

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if es_primo(matriz[fila][columna]):
            matriz[fila][columna] =  (int(matriz[fila][columna])*2)

print(matriz)
            




