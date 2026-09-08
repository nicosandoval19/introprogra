# ------------------------------------------------------------
# Ejercicio 10: buscar estudiante
# ------------------------------------------------------------
# Define una función buscar_estudiante(estudiantes, nombre_buscado)
# Recibe una lista de listas:
# [[nombre, puntaje], [nombre, puntaje], ...]
# Retorna el puntaje del estudiante buscado.
# Si no está, retorna "No encontrado".

def buscar_estudiante(estudiantes,nombre_buscado):
    for f in range(len(estudiantes)):
        for c in range(len(estudiantes[f])):
            if estudiantes[f][0]==nombre_buscado:
                return estudiantes[f][1] 
    return "No encontrado"

print("Ejercicio 10")
datos = [["Nico", 80], ["Sofia", 95], ["Pedro", 70]]
print(buscar_estudiante(datos, "Sofia"))   # esperado: 95
print(buscar_estudiante(datos, "Pedro"))   # esperado: 70
print(buscar_estudiante(datos, "Camila"))  # esperado: No encontrado