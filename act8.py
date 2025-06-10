import math

def area_circulo(radio):
    return math.pi*radio**2

def volumen_cilindro(radio, alto):
    area_base=area_circulo(radio)
    return area_base*altura

radio=0
altura=0

print("Ingrese el radio del círculo en cm")
radio=int(input())

print("Ingrese la altura del cilindro en cm")
altura=int(input())

area=area_circulo(radio)
volumen=volumen_cilindro(radio, altura)

print("El área del círculo es: ", area, "cm")

print("El volumen del cílindro es: ", volumen, "cm")  