from datetime import datetime

def calculo_edad_dias(fecha_nacimiento):
    fecha_actual=datetime.today()
    edad_dias=(fecha_actual-fecha_nacimiento).days
    return edad_dias

def calculo_edad(fecha_nacimiento):
    fecha_actual=datetime.today()
    año=fecha_actual.year-fecha_nacimiento.year
    mes=fecha_actual.month-fecha_nacimiento.month
    dia=fecha_actual.day-fecha_nacimiento.day
    if dia<0:
        mes-=1
        dia+=(datetime(fecha_actual.year, fecha_actual.month, 1)-datetime(fecha_actual.year, fecha_actual.month-1, 1)).days
    if mes<0:
        año-=1
        mes+=12
        
    return año, mes, dia


fecha_int=input("Ingresa tu fecha de nacimiento (dd/mm/aaaa):")

fecha_nacimiento=datetime.strptime(fecha_int,"%d/%m/%Y")

edad_dias=calculo_edad_dias(fecha_nacimiento)
año, mes, dia=calculo_edad(fecha_nacimiento)

print("Edad en días:", edad_dias, "días.")
print("Edad:", año, "años", mes, "meses", dia, "días")