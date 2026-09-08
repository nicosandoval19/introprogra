# =========================
# EJERCICIO 7
# =========================
# Recibirás una matriz cuadrada representada
# como lista de listas.
#
# Debes crear una lista con los elementos
# de la diagonal principal.
#
# Finalmente, imprime la lista resultante.

matriz = eval(input())

# Tu código aquí
lista_diagonal=[]

#[[ 1,2,3],[4,5,6],[7,8,9]]

#es decir 1,5,9

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if fila==columna:
            numero=(int(matriz[fila][columna]))
            lista_diagonal.append(numero)

print(lista_diagonal)


        
    
