# Secuencias de escape
#backslash \ es un caracter de escape, se utiliza para representar caracteres especiales en una cadena de texto.
#\" representa una comilla doble dentro de una cadena de texto delimitada por comillas dobles.
#\' representa una comilla simple dentro de una cadena de texto delimitada por comillas simples.
#\\ representa una barra invertida literal.
#\n representa un salto de línea.
#\t representa una tabulación."

curso="Python \ndesde \ncero"
#nombre= input(str())
#apellido= input(str())
print("indique su nombre")
nombre= input(str())
print("indique su apellido")
apellido= input(str())
print("su nombre y apellido es:")
print(nombre+"\n"+apellido)
print(nombre+"\t"+apellido) 