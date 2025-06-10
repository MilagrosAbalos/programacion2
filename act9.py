def calcular_factura(factura, iva):   
    if(iva==0):
        iva=(21*factura)/100
        total=factura+iva
    else:
        iva=(iva*factura)/100
        total=factura+iva
    return total
factura=0
iva=0
factura=int(input("Ingrese la cantidad de la factura:"))
iva=int(input("Ingrese el IVA a aplicar. Si no tiene ese dato ingrese 0:"))

total=calcular_factura(factura, iva)
print("El total de la factura con IVA es:$", total)
    