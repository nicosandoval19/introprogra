

for numero in range(5):
    print(numero, "Hola mundo")

buscar=6
for numero in range(5):#iterable es una secuencia de elementos que se pueden recorrer, como listas, tuplas, diccionarios, conjuntos, cadenas de texto, etc.
    print(numero)
    if numero==buscar:
        print("encontrado",numero)
        break
else:
    print("no encontrado:( ")



for char in "Hola mundo":
    print(char)
    if char=="a":
        print(" Aqui hay una letra a!")
    else:
        print("No es una letra a")
    


