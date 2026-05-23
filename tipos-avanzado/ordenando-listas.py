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








while fichas>0:
    rint(tirada)

    #print(concentracion_sietes)
    
    
    if tirada=="7":
        fichas-=1
        concentracion_sietes+=1
        concentracion_asteriscos=0
    if concentracion_sietes==3:
        print("Ganaste $500!")
        dinero+=500
    elif tirada=="*":
        fichas-=1
        concentracion_asteriscos+=1
        concentracion_sietes=0
    if concentracion_asteriscos==3:
        fichas+=9
        print("- conseguiste 3 fichas!")
    else:
        concentracion_asteriscos=0
        concentracion_sietes=0
        fichas-=1
    
    if fichas%3==0 or fichas%3==1:
        print("- Quedan "+str(fichas//3)+" fichas")
    tirada=input()

print(dinero)
