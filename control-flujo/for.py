
b=3.95
a=float(input())
contador=0


for n in range (6):
    if contador==0:
        contador+=1
        if a <= b:
            print("True") 
        
        else:
            print("False")
        
    elif contador==1:
        contador+=1
        if a < b:
            print("True") 
        else:
            print("False")
    
    elif contador==2:
        contador+=1
        if a >= b:
            print("True")
        else:
            print("False")

    elif contador==3:
        contador+=1
        if a > b:
           print("True")
        else:
            print("False")
    
    elif contador==4:
        contador+=1
        if a == b:
            print("True")
        else:
            print("False")
    
    elif contador==5:
        contador+=1
        if a != b:
            print("True")
        else:
            print("False")
