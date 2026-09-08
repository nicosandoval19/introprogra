# ------------------------------------------------------------
# Ejercicio 4: limpiar texto
# ------------------------------------------------------------
# Define limpiar_texto(texto)
# Recibe un string.
# Debe retornar un nuevo string sin espacios y en minúscula.
#
# Ejemplo:
# "Ho La" -> "hola"

def limpiar_texto(texto):
    palabra_mostrar=texto.replace(" ","").lower()
    #print(palabra_mostrar)

    return palabra_mostrar

print("Ejercicio 4")
print(limpiar_texto("Ho La"))              # esperado: hola
print(limpiar_texto("Pro Gra Ma Cion"))    # esperado: programacion
print(limpiar_texto("OSO"))                # esperado: oso
print(limpiar_texto("A b C d"))            # esperado: abcd
