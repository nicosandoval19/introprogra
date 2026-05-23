# EJERCICIO NÚMEROS PRIMOS
# Recibir un string con números enteros separados por comas.
#
# Convertir los números en una lista de enteros.
#
# Crear una función para verificar si un número es primo:
# - un número primo solo es divisible por 1 y por sí mismo
# - probar divisores desde 2 hasta numero - 1
#
# Recorrer la lista:
# - si el número es primo, reemplazarlo por su doble
# - si no es primo, dejarlo igual
#
# Finalmente imprimir la lista modificada.
#
# Ejemplo:
# Entrada: 5,5,8,12,13,3
# Salida: [10, 10, 8, 12, 26, 6]


# Aqui puedes empezar a programar 😀
numeros=input()

numeros_bien= numeros.split(",")

#print(numeros_bien)
lista_mumeros_final=[]

#for numero in numeros_bien:
    #if int(numero) % 2 == 0:
        #numeros2=(int(numero))
        
        #lista_mumeros_final.append(numeros2)
    #else:
        #print(numero)
        #numero2=(int(numero)+int(numero))
        #lista_mumeros_final.append(numero2)

#print(lista_mumeros_final)


#divisores_totales=0



for numero in numeros_bien:
    divisores_totales=0
    for i in range(int(numero)+1):
        divisores=(int(numero)%(1+int(numero)-int(i)))
        #print(i)
        #print(divisores)
        if divisores==0:
            divisores_totales+=1
        #print(divisores)
    if divisores_totales>=3:
        numeros2=(int(numero))
        lista_mumeros_final.append(numeros2)
    else:
        numero2=(int(numero)+int(numero))
        lista_mumeros_final.append(numero2)
        
    #print(divisores_totales)
print(lista_mumeros_final)


