mascotas =["perro", "gato", "pajaro"]
print(mascotas)
print(mascotas[0]) #imprime el primer elemento de la lista
mascotas[0] = "conejo" #cambia el primer elemento de la lista por "conejo"
print(mascotas[1]) #imprime el segundo elemento de la lista
print(mascotas[2]) #imprime el tercer elemento de la lista
print(mascotas[-1]) #imprime el ultimo elemento de la lista
print(mascotas[-2]) #imprime el penultimo elemento de la lista
print(mascotas[-3]) #imprime el antepenultimo elemento de la lista
print(mascotas[0:2]) #imprime los elementos desde el indice 0 hasta el indice 2 (excluyendo el indice 2)
print(mascotas[1:3]) #imprime los elementos desde el indice 1 hasta el indice 3 (excluyendo el indice 3)


print(mascotas[::2]) #imprime los elementos desde el indice 0 hasta el final de la lista, saltando de 2 en 2


numeros= list(range(21))
print(numeros[1::2]) #imprime los numeros desde el indice 1 hasta el final de la lista, saltando de 2 en 2 (imprime los numeros impares)