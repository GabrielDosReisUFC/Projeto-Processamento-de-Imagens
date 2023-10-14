from PIL import Image
from numpy import asarray;

def inverter(path,salvar):
    img = Image.open(path)
    data = asarray(img) / 255.0
    data = (1 - data)*255
    img2 = Image.fromarray(data)
    img.close()
    img2.save(salvar)
    img2.close()
