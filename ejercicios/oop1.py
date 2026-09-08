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
                return int(l)
            else:
                contador+=1

    else:
        for l in str(numero):
            if indice == contador:
                return int(l)
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
                return int(lista_final)
                
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

contra_original = int(input())
contra2 = contra_original
numerox = int(input())

par_o_impar = cantidad_de_digitos(contra_original)

lista = []
for n in str(contra_original):
    lista.append(str(n))

for l in range(0,numerox):
    if par_o_impar % 2 != 0:
        contra2+=2
        contra2**=contra2
        numero_cambiar=contra2%10
        lista.reverse()
        lista[l]=str(numero_cambiar)
        lista.reverse()
        numero_final = "".join(lista)
        
    
     
    
    else:
        contra2+=2
        contra2**=contra2
        numero_cambiar=contra2%10
        lista[int(l)]=numero_cambiar
        numero_final = "".join(lista)

print(numero_final)