

# ------------------------------------------------------------
# Ejercicio 6: invertir texto
# ------------------------------------------------------------
# Define una función invertir_texto(texto)
# Retorna el texto al revés.
# Intenta hacerlo con for, no con [::-1].

def invertir_texto(texto):
    lista=[]
    for l in texto:
        lista.insert(0,l)
    lista_retornar="".join(lista)
    return lista_retornar

    

    
   

print("Ejercicio 6")
print(invertir_texto("hola"))       # esperado: aloh
print(invertir_texto("python"))     # esperado: nohtyp
print(invertir_texto("oso"))        # esperado: oso
print(invertir_texto("abc"))        # esperado: cba