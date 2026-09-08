# ------------------------------------------------------------
# Ejercicio 2: suma de dígitos en posiciones pares
# ------------------------------------------------------------
# Define suma_posiciones_pares(numero)
# Recibe un número entero positivo.
# Retorna la suma de los dígitos que están en posiciones pares,
# contando desde la izquierda y partiendo desde 0.
#
# Ejemplo: 57291
# posiciones: 0 1 2 3 4
# dígitos:    5 7 2 9 1
# suma = 5 + 2 + 1 = 8


def suma_posiciones_pares(numero):
    lista=[]

    for l in str(numero):
          lista.append(l)
    #print (lista)

    suma = 0
    for c in lista[::2]:
         suma+=int(c)
    return suma
         
         
    
            
                  
    

print("Ejercicio 2")
print(suma_posiciones_pares(57291))    # esperado: 8
print(suma_posiciones_pares(123456))   # esperado: 9
print(suma_posiciones_pares(9090))     # esperado: 18
print(suma_posiciones_pares(7))        # esperado: 7
