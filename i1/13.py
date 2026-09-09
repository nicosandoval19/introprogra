# ------------------------------------------------------------
# Ejercicio 3: clave alternada
# ------------------------------------------------------------
# Define clave_alternada(texto)
# Retorna True si las letras del texto alternan entre vocal y consonante.
# Considera solo letras minúsculas y sin espacios.
#
# Ejemplo:
# "casa" -> c(consonante), a(vocal), s(consonante), a(vocal) -> True
# "perro" -> p(consonante), e(vocal), r(consonante), r(consonante) -> False


def clave_alternada(texto):
    vocal ="aAeEiIoOuU"
    consonante = "bcdfghjklmnñpqrstvwxyz"
    anterior=""

    for l in str(texto):
        if l in vocal and anterior=="consonante":
            anterior="vocal"
        elif l in consonante and anterior=="vocal":
            anterior="consonante"
        elif anterior=="" and l in vocal:
            anterior ="vocal"
        elif anterior=="" and l in consonante:
            anterior="consonante"
        else:
            return False
    return True

print("Ejercicio 3")
print(clave_alternada("casa"))      # esperado: True
print(clave_alternada("perro"))     # esperado: False
print(clave_alternada("amigo"))     # esperado: False
print(clave_alternada("banana"))    # esperado: True

