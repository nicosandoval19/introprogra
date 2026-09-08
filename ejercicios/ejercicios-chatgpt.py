# En una plataforma de música, cada canción está representada por una letra.
#
# canciones = ["R", "P", "T", "S"]
#
# Cada usuario tiene un string con las canciones que escuchó:
#
# usuarios = ["RPT", "TS", "RR", "", "SPT"]
#
# Objetivo
# Debes crear la función mas_escuchada(canciones, usuarios),
# que retorne una lista:
#
# [letra, cantidad]
#
# donde:
# - letra es la canción más escuchada
# - cantidad es la cantidad de usuarios que escucharon esa canción
#
# IMPORTANTE:
# - Si una canción aparece varias veces en un mismo string,
#   cuenta solo una vez para ese usuario.
# - Siempre existirá una única canción más escuchada.
#
# Ejemplo:
#
# canciones = ["R", "P", "T", "S"]
# usuarios = ["RPT", "TS", "RR", "", "SPT"]
#
# Retorna:
#
# ["T", 3]


def mas_escuchada(canciones, usuarios):

    cantidad=0
    nombreCancion=""

    for cancion in canciones:
        

        contador=0
        

        for usario in usuarios:
            
            

            if cancion in usario :
                contador+=1
               


    
        if contador>cantidad:
            cantidad=contador
            nombreCancion=cancion
        
    return(cantidad,nombreCancion)
        

canciones = ["R", "P", "T", "S"]
usuarios = ["RPT", "TS", "RR", "", "SPT"]


print(mas_escuchada(canciones, usuarios))