# ------------------------------------------------------------
# Ejercicio 2: es par
# ------------------------------------------------------------
# Define una función es_par(numero)
# Retorna True si el número es par.
# Retorna False si el número es impar.

def es_par(numero):
    if numero % 2 ==0:
        return True
    return False

print("Ejercicio 2")
print(es_par(4))     # esperado: True
print(es_par(7))     # esperado: False
print(es_par(0))     # esperado: True
print(es_par(15))    # esperado: False