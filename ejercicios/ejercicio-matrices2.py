# OBJETIVO:
# Debes descubrir el mensaje secreto.
#
# PASO 1:
# Usa las coordenadas de nums para sacar letras desde lets.
#
# PASO 2:
# Las letras obtenidas NO están en el orden correcto.
# Debes usar pos para mover cada letra a su posición final.
#
# PASO 3:
# Une las letras para formar una sola palabra y retornarla.


lets = [
    ['M', 'P', 'T', 'A'],
    ['R', 'O', 'L', 'E'],
    ['S', 'I', 'N', 'U'],
    ['C', 'D', 'H', 'F']
]

nums = [
    [0,0],
    [1,1],
    [2,2],
    [1,2]
]

pos = [3,1,0,2]


def palermo(lets, nums, pos):
    
    lista_letras=[]
    lista_para_ordenar=[""] * len(pos)
    
    for numero in nums:
        fila=numero[0]
        columna=numero[1]

        lista_letras.append(lets[fila][columna])

    for i in range(len(pos)):
        letra=lista_letras[i]
        posi=pos[i]
        lista_para_ordenar[posi]=letra

    palabra="".join(lista_para_ordenar)
    return palabra


    # AQUÍ VA TU CÓDIGO

    pass


print(palermo(lets, nums, pos))