# ------------------------------------------------------------
# Ejercicio 10: rotar texto
# ------------------------------------------------------------
# Define rotar_texto(texto, n)
# Retorna el texto moviendo los primeros n caracteres al final.
#
# Ejemplo:
# rotar_texto("abcdef", 2) -> "cdefab"

def rotar_texto(texto,n):
    ultimos_n= texto[0:n]
    #print(ultimos_n)
    restante=texto[n::]

    entregar=restante+ultimos_n

    return entregar


print("Ejercicio 10")
print(rotar_texto("abcdef", 2))     # esperado: cdefab
print(rotar_texto("programa", 3))   # esperado: gramapro
print(rotar_texto("hola", 1))       # esperado: olah
print(rotar_texto("python", 0))     # esperado: python