# =========================
# EJERCICIO 4
# =========================
# Recibirás una matriz representada como
# lista de listas.
#
# Debes reemplazar todos los números
# negativos por 0.
#
# Finalmente, imprime la matriz resultante.

matriz = eval(input())
#print(len(matriz))

# Tu código aquí
#input=[[1,-2],[3,-4]]

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if (int(matriz[fila][columna]) < (0)):
            matriz[fila][columna]=0
            
           
        
            

        
        
print(matriz)




            

#print(matriz)            
            
    