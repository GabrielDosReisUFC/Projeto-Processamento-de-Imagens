from PIL import Image
import numpy;
from numpy import asarray;
import retornarPath

def transformacao_logaritmica(string):
    img = Image.open(string)
    data = asarray(img)
    c = 255 / numpy.log(1 + numpy.max(data))
    s = c * numpy.log(1+data)
    s = s.astype(numpy.uint8)
    img2 = Image.fromarray(s)
    img.close()
    return retornarPath.path(string,img2)