from PIL import Image
from numpy import asarray;
import retornarPath

def inverter(string):
    img = Image.open(string)
    data = asarray(img) / 255.0
    data = (1 - data)*255
    img2 = Image.fromarray(data)
    img.close()
    return retornarPath.path(string,img2)