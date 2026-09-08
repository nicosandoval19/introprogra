# ------------------------------------------------------------
# Ejercicio 9: filtrar aprobados
# ------------------------------------------------------------
# Define una función aprobados(estudiantes)
# Recibe una lista de listas con formato:
# [[nombre, nota], [nombre, nota], ...]
# Retorna una lista con los nombres de quienes tienen nota >= 4.0.


def aprobados(estudiantes):
    lista_nombres =[]
    for fila in range(len(estudiantes)):
        #print(estudiantes[fila])
        for columna in range(len(estudiantes[fila])):
            if estudiantes[fila][1]>=4.0:
                if estudiantes[fila][0] not in lista_nombres:

                    lista_nombres.append(estudiantes[fila][0])
            #print(estudiantes[fila][0])

        #for columna in range(len(estudiantes[fila])):
            #print(estudiantes[fila][columna])
    return lista_nombres

print("Ejercicio 9")
print(aprobados([["Nico", 5.5], ["Sofia", 3.9], ["Pedro", 4.0]]))
# esperado: ["Nico", "Pedro"]

print(aprobados([["Ana", 2.0], ["Luis", 6.0], ["Marta", 4.5]]))
# esperado: ["Luis", "Marta"]