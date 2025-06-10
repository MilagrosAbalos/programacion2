from datetime import date

def calculo_edad_dias(fecha_nacimiento):
    fecha_actual=date.today()
    edad_dias=(fecha_actual-fecha_nacimiento).days
    return edad_dias

año_nacimiento=int(input("Ingrese el año de nacimiento (YYYY):"))
mes_nacimiento=int(input("Ingrese el año de nacimiento (YYYY):"))
dia_nacimiento=int(input("Ingrese el año de nacimiento (YYYY):"))
fecha_nacimiento=date(año_nacimiento, mes_nacimiento, dia_nacimiento)

edad_dias=calculo_edad_dias(fecha_nacimiento)
print("Edad en días:", edad_dias, "días.")