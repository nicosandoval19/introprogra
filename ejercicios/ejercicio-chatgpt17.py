# =========================
# PREGUNTA — DCC-Sopa de números 🍜
# =========================
#
# En el DCC ahora existe un nuevo juego llamado
# DCC-Sopa de números 😨.
#
# Cada jugador tiene un tablero representado
# como una matriz de 4x4 con números enteros.
#
# Además, existe una lista llamada encontrados
# que contiene números encontrados por el sistema.
#
# Tu objetivo será definir la función:
#
# def buscar(tablero, encontrados):
#
# La función recibirá:
#
# - tablero:
#   una lista de listas de enteros representando
#   el tablero del jugador.
#
# - encontrados:
#   una lista de enteros con números detectados
#   por el sistema.
#
# La función deberá retornar un int indicando
# cuántos números de encontrados aparecen
# dentro del tablero.
#
# Tu misión es únicamente definir la función,
# los test cases harán uso de ella posteriormente.
#
# Ejemplo:
#
# tablero = [[3,8,12,20],
#            [7,14,25,30],
#            [1,9,18,27],
#            [5,11,22,31]]
#
# encontrados = [2,7,9,15,22]
#
# print(buscar(tablero, encontrados))
#
# Output:
# 3
#
# Explicación:
# Los números 7, 9 y 22 se encuentran dentro
# del tablero, por lo tanto la función retorna 3.


def buscar(tablero, encontrados):
    final=0
    for numero in (encontrados):

        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                if numero== tablero[fila][columna]:
                    final+=1 

            
    return(final)
    
        


#for fila in range(len(matriz)):
    #for columna in range(len(matriz[fila])):
        #if buscar((matriz[fila][columna]),encontrados):
            #hola=hola

#print(final)

tablero = [[3,8,12,20],
           [7,14,25,30],
           [1,9,18,27],
           [5,11,22,31]]

encontrados = [2,7,9,15,22]

print(buscar(tablero, encontrados))








# Tu código aquí
 