#numero= 1
#while numero < 100:
    #print(numero)
    #numero *= 2

#comando = ""

#while comando.lower() !="salir":
    #comando = input("$ ")
    #print(comando)
#print("¡Hasta luego!")

while True:#lo utilizamos para crear un bucle infinito, es decir, que se ejecute hasta que se cumpla una condición de ruptura en este caso cuando el usuario escriba "salir" el loop se detendrá       
    comando = input("$ ")
    if comando.lower() == "salir":
        break
    #print(comando)
print("¡Hasta luego!")
