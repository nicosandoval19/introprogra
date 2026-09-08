# ------------------------------------------------------------
# Ejercicio 9: reemplazar solo una aparición
# ------------------------------------------------------------
# Define reemplazar_en_posicion(texto, indice, nuevo)
# Recibe un string, un índice y un nuevo carácter.
# Retorna el texto con el carácter de esa posición reemplazado.
#
# Ejemplo:
# reemplazar_en_posicion("banana", 1, "o") -> "bonana"


def reemplazar_en_posicion(texto,indice,nuevo):
    lista = []
    for l in str(texto):
        lista.append(l)

    lista[indice]=nuevo

    entregar = "".join(lista)

    return entregar

print("Ejercicio 9")
print(reemplazar_en_posicion("banana", 1, "o"))   # esperado: bonana
print(reemplazar_en_posicion("aaaa", 2, "x"))     # esperado: aaxa
print(reemplazar_en_posicion("python", 0, "P"))   # esperado: Python
print(reemplazar_en_posicion("hola", 3, "x"))     # esperado: holx
