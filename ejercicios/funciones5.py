# ------------------------------------------------------------
# Ejercicio 3: suma de dígitos
# ------------------------------------------------------------
# Define una función suma_digitos(numero)
# Recibe un número entero positivo.
# Retorna la suma de sus dígitos.
# Ejemplo: 123 -> 1 + 2 + 3 = 6


def suma_digitos(numero):
    contador=0
    for l in str(numero):
        contador+=int(l)
    return contador

print("Ejercicio 3")
print(suma_digitos(123))      # esperado: 6
print(suma_digitos(9090))     # esperado: 18
print(suma_digitos(5))        # esperado: 5
print(suma_digitos(11111))    # esperado: 5
