# EJERCICIO DIGIPET
# Recibir 2 strings separados por comas:
# 1. Nombre y peso del digipet.
# 2. Cantidad de alimento por kg, precio por kg, hora y minutos.
#
# Guardar los datos en 2 listas:
# digipet = [nombre, peso]
# informacion = [alimento_por_kg, precio_kg, hora, minutos]
#
# Calcular:
# - Cantidad total de alimento:
#   peso * alimento_por_kg
#
# - Precio total:
#   alimento_total * precio_kg
#
# Imprimir:
# "Lista de compras del digipet {nombre}"
# "El digipet necesita {cantidad} kg de alimento"
# "Costo total: ${precio}"
# "Alarma: {hora} : {minutos}"




nombre= input()
peso=input()
lista_separada= nombre.split(",")
lista_separada2= peso.split(",")

print("Lista de compras del digipet "+ lista_separada[0])
primer_termino= lista_separada[1]
segundo_termino= lista_separada2[0]
tercer_termino= lista_separada2[1]
multiplicacion=(int(primer_termino)*int(segundo_termino))
multiplicacion2=(int(primer_termino)*int(segundo_termino)*int(tercer_termino))
print("El digipet necesita "+str(multiplicacion)+" kg de alimento")
print("Costo total: "+ "$"+ str(multiplicacion2))
print("Alarma: "+lista_separada2[2]+" : "+lista_separada2[3])
