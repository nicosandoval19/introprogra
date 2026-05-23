# EJERCICIO DARK WEB - DIGIPET
# Leer nombres de enemigos indefinidamente hasta recibir "FIN".
# Guardar todos los enemigos en una lista.
#
# Luego leer el nombre del enemigo objetivo.
#
# Recorrer la lista eliminando enemigos desde el inicio usando pop(0).
#
# Si el enemigo eliminado NO es el objetivo:
# - imprimir la lista resultante sin ese enemigo
# - agregar el enemigo al final de la lista
#
# Si el enemigo eliminado SÍ es el objetivo:
# - imprimir "Enemigo aniquilado!"
# - imprimir la lista final sin el enemigo eliminado
# - terminar el ciclo
#
# Importante:
# - la lista se modifica dinámicamente
# - se rota moviendo enemigos al final
# - el objetivo desaparece definitivamente de la lista


nombre=input()
#nombres_enemigos=input()

lista=[]

while nombre!= "FIN":
    lista.append(nombre)
    nombre=input()
    

nombre_enemigos=input()


#print(lista)
while lista:
    if lista[0]==nombre_enemigos:
        listas=lista.pop(0)
        
        break
    else:
        listas= lista.pop(0)
        print(lista)
        lista.append(listas)
print("Enemigo aniquilado!")
print(lista)


#print(nombre_enemigos)


    #if lista[0]==nombre_enemigos:
    #print("Enemigo aniquilado!")
#else:
    #lista.pop[0]
#print(lista)
