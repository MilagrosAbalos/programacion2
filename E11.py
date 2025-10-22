from random import randint

lista=["Cele", "More", "Ange", "Elvis", "Tomas S", "Tomas R", "Brisa", "Bere", "Theo", "Mili"]

lista_expo=list()

while lista:
    estudiante_ind=randint(0, len(lista)-1)
    est_aleatorio=lista[estudiante_ind]
    lista_expo.append(est_aleatorio)
    lista.pop(estudiante_ind)

print("Lista para la exposición")
for i, estudiante in enumerate(lista_expo, start=1):
    print(i, "." , estudiante)

                                        