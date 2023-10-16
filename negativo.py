from PIL import Image
import numpy as np

def inverter(path,salvar):
    img = Image.open(path)
    data = asarray(img) / 255.0
    data = (1 - data)*255
    img2 = Image.fromarray(data)
    img.close()
    img2.save(salvar)
    img2.close()

def negativo_RGB(path, salvar):
    img = Image.open(path)
    data = np.array(img)
    inverted_data = 255 - data
    img2 = Image.fromarray(inverted_data)
    img.close()
    img2.save(salvar)
    img2.close()