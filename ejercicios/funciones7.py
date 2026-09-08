# ------------------------------------------------------------
# Ejercicio 5: contar repetidos
# ------------------------------------------------------------
# Define una función contar_apariciones(lista, elemento)
# Retorna cuántas veces aparece elemento dentro de lista.

def contar_apariciones(lista,elemento):
    contador =0

    for l in lista:
        if l == elemento:
            contador+=1
    return contador




