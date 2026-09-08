# ------------------------------------------------------------
# Ejercicio 6: comprimir texto
# ------------------------------------------------------------
# Define comprimir_texto(texto)
# Recibe un string y retorna otro string indicando cada letra
# seguida de cuántas veces aparece consecutivamente.
#
# Ejemplo:
# "aaabbc" -> "a3b2c1"
# "hhhhola" -> "h4o1l1a1"

def comprimir_texto(texto):
    lista=[]
    lista_normal = []
    lista_entrega =[]
    
    for l in texto:
        if l not in lista:

            lista.append(l)
        lista_normal.append(l)


    for l in lista:
        contador=0
        lista_entrega.append(l)
        for c in lista_normal:
            if l==c:
                contador+=1
        lista_entrega.append(str(contador))

    juntas="".join(lista_entrega)
    return juntas

print("Ejercicio 6")
print(comprimir_texto("aaabbc"))      # esperado: a3b2c1
print(comprimir_texto("hhhhola"))     # esperado: h4o1l1a1
print(comprimir_texto("abc"))         # esperado: a1b1c1
print(comprimir_texto("zzzzaa"))      # esperado: z4a2

   

    