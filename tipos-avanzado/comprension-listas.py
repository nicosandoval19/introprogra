usuarios = [["Alice", 4], ["Bob", 1], ["Charlie", 3], ["David", 2]] 

#nombres=[]
#for usuario in usuarios:
    #nombres.append(usuario[0])#agrega el primer elemento de cada sublista a la lista nombres
#print(nombres)

nombres=[usuario[0] for usuario in usuarios]#agrega el primer elemento de cada sublista a la lista nombres usando una comprension de listas
print(nombres)