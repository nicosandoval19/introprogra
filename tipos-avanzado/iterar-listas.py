mascotas= ["perro", "gato", "pez", "hamster"]
for mascota in mascotas:
    print(mascota)

for mascota in enumerate(mascotas):
    print(mascota)

for mascota in enumerate(mascotas):
    print(mascota[0])

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)