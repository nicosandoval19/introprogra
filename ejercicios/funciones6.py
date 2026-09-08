# ------------------------------------------------------------
# Ejercicio 4: mayor de una lista
# ------------------------------------------------------------
# Define una función mayor_lista(lista)
# Recibe una lista de números.
# Retorna el número mayor.
# No uses max().


def mayor_lista(lista):
    contador=0
    for l in lista:
        if contador==0:
            contador=int(l)
        elif int(l)>contador:
            contador=int(l)
    return contador


print("Ejercicio 4")
print(mayor_lista([1, 5, 3, 2]))       # esperado: 5
print(mayor_lista([10, 7, 20, 4]))     # esperado: 20
print(mayor_lista([-3, -10, -1]))      # esperado: -1
print(mayor_lista([8]))                # esperado: 8
