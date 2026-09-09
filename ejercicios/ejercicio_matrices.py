# EJERCICIO

# Debes definir la función:
# puede_colocarse(tablero, pieza)
#
# La función debe retornar:
# True  -> si TODAS las coordenadas están vacías (valor 0)
# False -> si alguna coordenada ya está ocupada


tablero = [[0, 0, 4, 4, 0],
           [0, 0, 0, 4, 0],
           [2, 0, 0, 0, 0],
           [2, 2, 0, 1, 1],
           [0, 0, 0, 0, 0]]

pieza = [[0,0], [1,0], [1,1], [2,1], [2,2]]



# ESCRIBE TU FUNCIÓN ABAJO
def puede_colocarse(tablero,pieza):
    
    for coordenada in pieza:
        fila=coordenada[0]
        columna=coordenada[1]

        if tablero[fila][columna]!=0:
            return False
    return True




# PRUEBA
print(puede_colocarse(tablero, pieza))