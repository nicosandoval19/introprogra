x=input("")
#int(x) #esto no se puede hacer porque x es un string y no se puede convertir a entero
#float(x) #esto no se puede hacer porque x es un string y no se puede
#convertir a entero
#str(x) #esto si se puede hacer porque x es un string y se puede convertir
#bool(x) #esto si se puede hacer porque x es un string y se puede convertir a booleano
print(bool(x)) #esto imprimira True porque cualquier string no vacio se considera verdadero en python
print(bool("")) #esto imprimira False porque un string vacio se considera falso en python
print(bool(0)) #esto imprimira False porque el numero 0 se considera falso en python
print(bool(1)) #esto imprimira True porque cualquier numero diferente de 0 se considera
#verdadero en python
