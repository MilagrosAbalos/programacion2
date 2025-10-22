from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("flor.jpeg")
im_gris = im.convert("L")
matriz = np.array(im_gris)

for fila in range(len(matriz)):
    for columna in range(len(matriz[0]) // 2):  
        ind_op = len(matriz[0]) - 1 - columna

        aux = matriz[fila, columna]
        matriz[fila, columna] = matriz[fila, ind_op]
        matriz[fila, ind_op] = aux
        

plt.imshow(matriz, cmap="gray")
plt.show()

 
                