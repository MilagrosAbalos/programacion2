M=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]

print("Matriz")
for fila in M:
    print(fila)
suma_p=0
mult_p=1

suma_c=0
mult_c=1
    
for i in range(4):
    suma_p += M[i][i]
    mult_p *= M[i][i]
    
    suma_c += M[i][3-i]
    mult_c *= M[i][3-i]
    
print("Suma diagonal principal:", suma_p)
print("Multiplicación diagonal principal", mult_p)

print("Suma contra diagonal:", suma_c)
print("Multiplicación contra diagonal", mult_c)