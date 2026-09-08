def cantidad_de_digitos(numero):
    contador1=0
    for l in str(numero):
        contador1+=1
    return contador1
    


def en_posicion(numero,indice,reversa):
    contador = 0
    if reversa == True:
        for l in str(numero)[::-1]:
            if contador == indice:
                return l
            else:
                contador+=1

    else:
        for l in str(numero):
            if indice == contador:
                return l
            else:
                contador+=1

def reemplazar(numero,indice,nuevo,reversa):
    contador =0
    lista =[]
    

    for c in str(numero):
        
        lista.append(c)

   

    if reversa == True:
        for l in (lista[::-1]):
            if contador == indice:
                lista.reverse()
                lista[indice]=str(nuevo)
                lista.reverse()
                lista_final="".join(lista)
                return lista_final
                
            else:
                contador+=1
    else:
        for l in lista:
            if indice == contador:
                lista[indice]=str(nuevo)
                numero_final= "".join(lista)
                
                

                
                return int(numero_final)
            else:
                contador+=1


print(reemplazar(1111, 2, 9, False))     # esperado: 1191
print(reemplazar(1111, 2, 9, True))      # esperado: 1911

print(reemplazar(7771237, 1, 4, False))  # esperado: 7471237
print(reemplazar(7771237, 1, 4, True))   # esperado: 7771247
