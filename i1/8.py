#Ejercicio 8: clave segura
# ------------------------------------------------------------
# Define clave_segura(clave)
# Recibe un string.
# Retorna True si cumple TODAS estas condiciones:
# - Tiene al menos 8 caracteres.
# - Tiene al menos una letra minúscula.
# - Tiene al menos una letra mayúscula.
# - Tiene al menos un número.
#
# No es necesario revisar símbolos.

def clave_segura(clave):
    contador=0
    mayus = 0
    numero = 0
    minus = 0

    for l in str(clave):
       contador+=1
    for l in clave:
       if l.islower():
          minus+=1
    for l in clave:
        if l.isupper():
          mayus+=1
    for l in clave:
         if l.isdigit():

            numero+=1

    if contador>=8:
       if mayus>=1 and numero>=1 and minus>=1:
          return True
    return False
    
print("Ejercicio 8")
print(clave_segura("Hola1234"))     # esperado: True
print(clave_segura("hola1234"))     # esperado: False
print(clave_segura("HOLA1234"))     # esperado: False
print(clave_segura("Hola12"))       # esperado: False
print(clave_segura("Programacion1"))# esperado: True

     

    

    
    

    
        