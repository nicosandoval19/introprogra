# =========================
# EJERCICIO 3
# =========================
# Los ayudantes quieren números grandes 😎
#
# Recibirás números enteros separados por coma.
# Todo número menor que 10 deberá sumarse con 10.
#
# Finalmente, imprime la lista resultante.
#
# Ejemplo:
#
# Input:
# 2,15,8,20
#
# Output:
# [12, 15, 18, 20]

entrada = input()

entradaSplit=entrada.split(",")
lista_vacia=[]

for numero in (entradaSplit):
    if (((int(numero)))<10):
        numero_sumado=((int(numero))+10)
        lista_vacia.append(numero_sumado)
    else:
        numero_normal=(int(numero))
        lista_vacia.append(numero_normal)

print(lista_vacia)


# Tu código aquí