numeros= [1,2,3,4,5,6,7,8,9,10] 
numeros.sort()#ordena la lista de menor a mayor
print(numeros)
numeros.sort(reverse=True)#ordena la lista de mayor a menor 
print(numeros)
sorted_numeros= sorted(numeros)#ordena la lista de menor a mayor y devuelve una nueva lista ordenada
print(sorted_numeros)
sorted_numeros_desc= sorted(numeros, reverse=True)#ordena la lista de mayor a menor y devuelve una nueva lista ordenada
print(sorted_numeros_desc)



#usuarios= [[4, "Alice"], [1, "Bob"], [3, "Charlie"], [2, "David"]]
#usuarios.sort()#ordena la lista de menor a mayor por el primer elemento de cada sublista
#print(usuarios)

def ordena(elemento):
    return elemento[1]#ordena la lista de menor a mayor por el segundo elemento de cada sublista
usuarios =[["Alice", 4], ["Bob", 1], ["Charlie", 3], ["David", 2]]

usuarios.sort(key=ordena)#ordena la lista de menor a mayor por el segundo elemento de cada sublista
print(usuarios)

usuarios.sort(key=ordena, reverse=True)#ordena la lista de mayor a menor por el segundo elemento de cada sublista
print(usuarios)




usuarios.sort(key=lambda el:el[1],reverse=True)#ordena la lista de mayor a menor por el segundo elemento de cada sublista usando una funcion lambda
print(usuarios)

usuarios.sort(key=lambda el:el[1])#ordena la lista de menor a mayor por el segundo elemento de cada sublista usando una funcion lambda
print(usuarios)