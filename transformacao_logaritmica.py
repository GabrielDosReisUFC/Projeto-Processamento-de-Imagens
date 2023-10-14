from PIL import Image
import numpy;
import numpy as np;

def transformacao_logaritmica(string,salvar):
    img = Image.open(string)
    data = np.array(img)
    c = 255 / numpy.log(1 + numpy.max(numpy.max(data)))
    nova_imagem = (c * numpy.log(1+data)).astype(np.uint8)
    img2 = Image.fromarray(nova_imagem)
    img.close()
    img2.save(salvar)
    img2.close()