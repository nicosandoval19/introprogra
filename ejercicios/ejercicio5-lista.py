# EJERCICIO COMPRAS DEL MES
# Recibir un string separado por comas con formato:
# "producto,cantidad,p1,p2,p3,..."
#
# Convertir el string en una lista usando split(",").
#
# La lista contiene:
# - posición 0: nombre del producto
# - posición 1: cantidad de unidades a comprar
# - desde posición 2 en adelante: precios disponibles
#
# Objetivo:
# elegir los precios más bajos según la cantidad pedida.
#
# Si cantidad = k, se deben sumar los k precios más baratos.
#
# Finalmente imprimir:
# "{producto}: ${pesos_totales}"
#
# Ejemplo:
# hotdog,3,250,150,90,100,10,40
# precios más bajos: 10, 40 y 90
# salida: hotdog: $140

while fichas>0:
    #print(tirada)

    #print(concentracion_sietes)
    
    
    if tirada=="7":
        fichas-=1
        concentracion_sietes+=1
        concentracion_asteriscos=0
        if concentracion_sietes==3:
            print("Ganaste $500!")
            dinero+=500
    elif tirada=="*":
        fichas-=1
        concentracion_asteriscos+=1
        concentracion_sietes=0
        if concentracion_asteriscos==3:
            fichas+=9
            print("- conseguiste 3 fichas!")
    else:
        concentracion_asteriscos=0
        concentracion_sietes=0
        fichas-=1
    
    if fichas%3==0 or fichas%3==1:
        print("- Quedan "+str(fichas//3)+" fichas")
    tirada=input()

print(dinero)