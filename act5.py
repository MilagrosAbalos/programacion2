c=0
e=0
ce=0
cs=0
print("¿Cuántos caramelos tiene para repartir?")
c=int(input())
print("¿Cuántos estudiantes son?")
e=int(input())

ce=c//e
cs=c-(ce*e)

print("Cada estudiante recibe ", ce, " caramelos.")
print("Sobran", cs, "caramelos.")