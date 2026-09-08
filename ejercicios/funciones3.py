# ============================================================
# EJERCICIOS DE FUNCIONES - PRÁCTICA INTRO A LA PROGRAMACIÓN
# ============================================================


# ------------------------------------------------------------
# Ejercicio 1: cantidad de vocales
# ------------------------------------------------------------
# Define una función contar_vocales(texto)
# Recibe un string y retorna cuántas vocales tiene.
# Considera solo vocales minúsculas: a, e, i, o, u.

def contar_vocales(texto):
    contador=0
    for l in texto:
        
        if l =="a" or l=="e" or l=="i" or l=="o" or l=="u":
            contador+=1
    return contador


print("Ejercicio 1")
print(contar_vocales("hola"))          # esperado: 2
print(contar_vocales("programacion"))  # esperado: 5
print(contar_vocales("python"))        # esperado: 1
print(contar_vocales("bcdfg"))         # esperado: 0