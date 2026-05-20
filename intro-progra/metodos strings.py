animal = " chanCHito feliz "
print(animal.upper())#convierte todo a mayuscula
print(animal.lower()) #convierte todo a minuscula
print(animal.capitalize())#co
print(animal.title())#cada palabra empieza con mayuscula
print(animal.rstrip())#quita los espacios a la derecha o a la izquierda respectivamente
print(animal.lstrip())#quita los espacios a la derecha o a la izquierda respectivamente
print(animal.find("cH"))#-1 significa que no lo encuentra
print(animal.replace("CH", "pu"))#reemplaza las ocurrencias de "CH" con "pu"
print("nCH" in animal) #devuelve True si "nCH" está presente en la cadena, de lo contrario devuelve False
print("nCH" not in animal) #devuelve True si "nCH" no está presente en la cadena, de lo contrario devuelve False
