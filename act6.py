b200=0
b1000=0
c=0
s=0
print("Ingrese la cantidad que desea extraer")
c=int(input())

b1000=c//1000

c=c-(b1000*1000)

b200=c//200

s=c-(b200*200)

print("Recibe ", b1000, " billetes de $1000 y ", b200, " billetes de $200.")
print("No se pudo extraer $", s)