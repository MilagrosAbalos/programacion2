import random
ns=random.randint(1,20)
ni=0
i=6

print("ADIVINE EL NÚMERO")
print("Tiene 6 intentos")
    
while(i>0):
    print("Ingrese el número")
    ni=int(input())
    
    if(ni==ns):
        print("¡Felicidades! El número es", ns)
        break
    
    elif(ni<ns):
        print("El número secreto es mayor que", ni)
    else:
        print("El número secreto es menor que", ni)
    
    i=i-1       
if(i==0):
    print("oh, perdió. El número es", ns)