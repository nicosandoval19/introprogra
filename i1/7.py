# ------------------------------------------------------------
# Ejercicio 7: número creciente
# ------------------------------------------------------------
# Define es_creciente(numero)
# Retorna True si los dígitos del número van de menor a mayor
# o se mantienen iguales.
#
# Ejemplo:
# 11239 -> True
# 321 -> False


def es_creciente(numero):
    

    

    numero_actual=0
    




    for l in str(numero):
        if int(l)>=numero_actual:
            numero_actual=int(l)
            
        else:
            return False
    return True

print("Ejercicio 7")
print(es_creciente(11239))    # esperado: True
print(es_creciente(1234))     # esperado: True
print(es_creciente(321))      # esperado: False
print(es_creciente(1111))     # esperado: True
print(es_creciente(908))      # esperado: False
    
            