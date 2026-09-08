# ------------------------------------------------------------
# Ejercicio 7: palíndromo
# ------------------------------------------------------------
# Define una función es_palindromo(texto)
# Retorna True si el texto se lee igual al derecho y al revés.
# Retorna False si no.
# Puedes usar la función invertir_texto.

def es_palindromo(texto):
    lista=[]
    for c in texto:
        lista.insert(0,c)
    lista_entregar = "".join(lista)
    if lista_entregar==texto:
        return True
    return False

print("Ejercicio 7")
print(es_palindromo("oso"))        # esperado: True
print(es_palindromo("reconocer"))  # esperado: True
print(es_palindromo("hola"))       # esperado: False
print(es_palindromo("python"))     # esperado: False
