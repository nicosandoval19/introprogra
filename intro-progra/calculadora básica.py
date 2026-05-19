print("Bienvenido a la calculadora basica, las operaciones disponibles son sumar, restar, multiplicar y dividir")

numero1=int(input("ingrese primer numero"))
numero2=int(input("ingrese segundo numero"))


print("Que operacion desea realizar?")
respuesta=input()
if respuesta=="sumar":
    resultado=numero1+numero2
    print("el resultado es",resultado)
elif respuesta=="restar":
    resultado=numero1-numero2
    print("el resultado es",resultado)
elif respuesta=="multiplicar":
    resultado=numero1*numero2
    print("el resultado es",resultado)
elif respuesta=="dividir":   
    if numero2==0:
        print("no se puede dividir por cero")

    else:
        resultado=numero1/numero2
        print("el resultado es",resultado)
else:    print("operacion no valida")

print("Gracias por usar la calculadora basica.")