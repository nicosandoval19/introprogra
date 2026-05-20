mascotas= ["perro", 
           "gato", 
           "pez", 
           "hamster"]



mascotas.insert(1, "conejo")#agrega en la posicion que se determine  el conejo, y desplaza a los demas a la derecha
print(mascotas)

mascotas.append("tortuga")#agrega al final de la lista
print(mascotas)






mascotas.remove("gato")#elimina el elemento gato de la lista
print(mascotas)

mascotas.pop(2)#elimina el elemento que se encuentra en la posicion 2, en este caso el pez
print(mascotas)

del mascotas[0]#elimina el elemento que se encuentra en la posicion 0, en este caso el perro
print(mascotas)
mascotas.clear()#elimina todos los elementos de la lista