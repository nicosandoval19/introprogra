# =========================
# EJERCICIO 1
# =========================
# Los ayudantes odian el número 5 😡
#
# Recibirás números enteros separados por coma.
# Debes guardar los números en una lista y
# reemplazar todos los 5 por 0.
#
# Finalmente, imprime la lista resultante.

entrada = input()

# Tu código aqu
nueva_lista=[]

entradaSplit=entrada.split(",")

for numero in (entradaSplit):
    print(numero)
    if numero=="5":
        
        
        nueva_lista.append(int(0))
    else:
        nueva_lista.append(int(numero))

print(nueva_lista)






