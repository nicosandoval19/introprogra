# ------------------------------------------------------------
# Ejercicio 3: dígito más repetido
# ------------------------------------------------------------
# Define digito_mas_repetido(numero)
# Recibe un número entero positivo.
# Retorna el dígito que aparece más veces.
# Si hay empate, retorna el que aparece primero en el número.
#
# Ejemplo: 331225
# el 3 aparece 2 veces, el 1 aparece 1, el 2 aparece 2, el 5 aparece 1.
# Hay empate entre 3 y 2, pero 3 aparece primero.
# Retorna 3.

def digito_mas_repetido(numero):
    contador_mas_alto = 0
    numero_mas_alto = 0
    
    for l in str(numero):
        contador=0
        #print(contador_mas_alto)
        #print(numero_mas_alto)
        #print("aaaaa")
        for c in str(numero):
            #print(c)
            if int(l)==int(c):
                contador+=1
                #print(contador)
                if contador>contador_mas_alto:
                    contador_mas_alto=contador
                    numero_mas_alto=l
                    #return numero_mas_alto
                elif contador==contador_mas_alto:
                    contador_mas_alto=contador_mas_alto
    return(numero_mas_alto)


print("Ejercicio 3")
print(digito_mas_repetido(331225))   # esperado: 3
print(digito_mas_repetido(122233))   # esperado: 2
print(digito_mas_repetido(987654))   # esperado: 9
print(digito_mas_repetido(555123))   # esperado: 5
        
