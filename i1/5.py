# ------------------------------------------------------------
# Ejercicio 5: palíndromo avanzado
# ------------------------------------------------------------
# Define es_palindromo_avanzado(texto)
# Debe retornar True si el texto es palíndromo ignorando espacios
# y diferencias entre mayúsculas y minúsculas.
#
# Ejemplo:
# "Anita lava la tina" debe retornar True.

def es_palindromo_avanzado(texto):
    lista_comparar=[]

    frase_sin_nada=texto.replace(" ","").lower()

    for l in frase_sin_nada:
        lista_comparar.insert(0,l)
    lista_entrar="".join(lista_comparar)

    #print(lista_entrar)
    if lista_entrar==frase_sin_nada:
        return True
    return False


print("Ejercicio 5")
print(es_palindromo_avanzado("Anita lava la tina"))  # esperado: True
print(es_palindromo_avanzado("Oso"))                 # esperado: True
print(es_palindromo_avanzado("Hola mundo"))          # esperado: False
print(es_palindromo_avanzado("Reconocer"))           # esperado: True