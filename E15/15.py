from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def escala_grises(imagen):
    R= imagen[:, :, 0]
    G= imagen[:, :, 1]
    B= imagen[:, :, 2]
    
    gris = R * 0.299 + G * 0.587 + B * 0.114
    
    gris_rgb = np.stack((gris, gris, gris), axis=2)
    
    return gris_rgb

im = Image.open("mariposas.jpeg")

im_array = np.array(im)

plt.imshow(im_array)
plt.show()

im_gris = escala_grises(im_array)

plt.imshow(im_gris.astype(np.uint8))
plt.show()