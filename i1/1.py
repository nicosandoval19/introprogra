# ============================================================
# FUNCIONES NIVEL INTERMEDIO / DIFÍCIL
# Intro a la Programación
# ============================================================


# ------------------------------------------------------------
# Ejercicio 1: contar dígitos pares
# ------------------------------------------------------------
# Define contar_pares(numero)
# Recibe un número entero positivo.
# Retorna cuántos dígitos pares tiene.
# Considera que 0 también es par.



def contar_pares(numero):
    contador = 0
    for l in str(numero):
        if int(l)%2==0:
            contador+=1 
    return contador


print("Ejercicio 1")
print(contar_pares(123456))    # esperado: 3
print(contar_pares(9090))      # esperado: 2
print(contar_pares(13579))     # esperado: 0
print(contar_pares(24680))     # esperado: 5
