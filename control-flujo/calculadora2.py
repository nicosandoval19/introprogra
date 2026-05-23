print("Bienvenido a la calculadora")
print("para salir ingresa 'salir'")
num1=""
num2=""
while True:
   
    if num1=="":
        num1 = input("Ingrese el primer número: ")
        if num1.lower() == "salir":
            break
        

        
        
        
    else:
        operacion = input("Ingrese la operación:")
        if operacion.lower() == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2  == "salir":
                break

        if operacion.lower() == "suma":
            resultado= float(num1)+float(num2)
            print("El resultado es: ", resultado)
            num1=resultado
            
           
            
          
        
        elif operacion.lower()=="resta":
            
            
            
            resultado = float(num1)-float(num2)
            print("El resultado es: ", resultado)
            num1=resultado
            
           
        elif operacion.lower()=="multiplicacion":
           
           
            resultado = float(num1)*float(num2)
            print("El resultado es: ", resultado)
            num1 = resultado
            
           
        
    
        elif operacion.lower()=="division":
            if num2 == "0":
                print("No se puede dividir por cero")
                continue
           
            
            resultado = float(num1)/float(num2)
            print("El resultado es: ", resultado)
            num1=resultado
           
            
     
    
    
