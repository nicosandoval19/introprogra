numeros = [1, 2, 3]

primero,segundo,tercero = numeros
print(primero,segundo,tercero)


primero, *otros = numeros
print(primero)
print(otros)

primero, segundo, *otros = numeros
print(primero,segundo)

print(otros)