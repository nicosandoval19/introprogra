# ------------------------------------------------------------
# Ejercicio 8: promedio de lista
# ------------------------------------------------------------
# Define una función promedio(lista)
# Recibe una lista de números.
# Retorna el promedio.
# No uses sum().

def promedio(lista):
    contador_numeros=0
    suma=0
    for l in lista:
        contador_numeros+=1
        suma+=l
    resultado=suma/contador_numeros
    return resultado

print("Ejercicio 8")
print(promedio([10, 20, 30]))      # esperado: 20.0
print(promedio([5, 5, 5, 5]))      # esperado: 5.0
print(promedio([1, 2, 3, 4]))      # esperado: 2.5