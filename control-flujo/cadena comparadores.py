edad = int(input("Ingrese su edad: "))

if 15 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")