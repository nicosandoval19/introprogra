# ==================================================
# EJERCICIO 4
# POTENCIA
# ==================================================

"""
Haz una función recursiva llamada potencia(base, exponente)
que calcule:

base^exponente

No puedes usar **.

Ejemplo:

potencia(2, 3)

Retorna:
8
"""

def potencia(base,exponente):
    if exponente==0:
       return 1
    else:
        return base* potencia(base,exponente-1)



base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

print(potencia(base, exponente))