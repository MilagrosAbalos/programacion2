def calcular_factorial(num):
    factorial=num
    for x in range(1,num,1):
        factorial=factorial*x
    return factorial

num=0
print("Para calcular factorial")
num=int(input("Ingrese el número que quiere calcular:"))

fact=calcular_factorial(num)
print("El factorial es", fact)