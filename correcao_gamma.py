from PIL import Image
import numpy;
from numpy import asarray;
import retornarPath

def gamma(string,gamma):
    img = Image.open(string)
    data = asarray(img)
    nova_imagem = numpy.power(data / 255.0, gamma) * 255.0
    img2 = Image.fromarray(nova_imagem)
    img.close()
    return retornarPath.path(string,img2)