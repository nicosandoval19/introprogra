# =========================
# EJERCICIO 2
# =========================
# Los ayudantes aman los números pares 😋
#
# Recibirás números enteros separados por coma.
# Debes duplicar todos los números pares
# de la lista.
#
# Finalmente, imprime la lista resultante.

entrada = input()

# Tu código aquí

entradaSplit= entrada.split(",")
lista_final=[]

for numero in (entradaSplit):
    if ((int(numero)) % 2) ==0:
        numeronuevo=((int(numero))*2)
        lista_final.append(numeronuevo)
    else:
        numeronuevo2=(int(numero))
        lista_final.append(numeronuevo2)

print(lista_final)
