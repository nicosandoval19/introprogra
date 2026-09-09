# ------------------------------------------------------------
# Ejercicio 2: suma de dígitos hasta encontrar cero
# ------------------------------------------------------------
# Define suma_hasta_cero(numero)
# Suma los dígitos del número desde la izquierda.
# Si aparece un 0, deja de sumar.
#
# Ejemplo:
# suma_hasta_cero(529034) -> 5 + 2 + 9 = 16


def suma_hasta_cero(numero):
    suma=0
    for l in str(numero):
        if int(l)==0:
            break
        else:
            suma+=int(l)
    return suma    

print("Ejercicio 2")
print(suma_hasta_cero(529034))      # esperado: 16
print(suma_hasta_cero(12345))       # esperado: 15
print(suma_hasta_cero(9087))        # esperado: 9
print(suma_hasta_cero(0))           # esperado: 0
