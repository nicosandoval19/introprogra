#and,or,not
#and ambos deben ser verdaderos para que el resultado sea verdadero
#or al menos uno debe ser verdadero para que el resultado sea verdadero
#not invierte el valor de verdad de una expresion

gas=True
encendido=True

if gas and encendido:
    print("puedes avanzar")

gas=False
encendido=True
if gas and encendido:
    print("puedes avanzar")
else:
    print("no puedes avanzar")

if gas or encendido:
    print("puedes avanzar")
else:    
    print("no puedes avanzar")


if not gas or encendido:
    print("puedes avanzar")