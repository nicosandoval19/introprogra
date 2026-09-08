# =========================
# EJERCICIO 3
# =========================
# Recibirás una matriz representada como
# lista de listas.
#
# Debes sumar todos los elementos
# de la matriz.
#
# Finalmente, imprime la suma.

matriz = eval(input())
lista_paraSuma=[]

# Tu código aquí

for k in matriz:
    for j in k:
        print(j)
        numero=(int(j))
        lista_paraSuma.append(numero)

print(sum(lista_paraSuma))

