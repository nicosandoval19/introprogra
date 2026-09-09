# ============================================================
# EJERCICIOS DIFÍCILES - FUNCIONES I1 INTRO PROGRAMACIÓN
# Temas: funciones, strings, ciclos, condiciones y números
# ============================================================


# ------------------------------------------------------------
# Ejercicio 1: contar dígitos mayores que X
# ------------------------------------------------------------
# Define contar_mayores(numero, x)
# Recibe un número entero positivo y un dígito x.
# Retorna cuántos dígitos del número son mayores que x.
#
# Ejemplo:
# contar_mayores(58391, 5) -> 2
# porque 8 y 9 son mayores que 5.



def contar_mayores(numero,x):
    contador = 0
    for l in str(numero):
        if int(l)>x:
            contador+=1
    return contador


print("Ejercicio 1")
print(contar_mayores(58391, 5))     # esperado: 2
print(contar_mayores(12345, 3))     # esperado: 2
print(contar_mayores(999, 8))       # esperado: 3
print(contar_mayores(1111, 1))      # esperado: 0