from PIL import Image
import numpy;
import numpy as np;

def transformacao_logaritmica(path,salvar):
    imagem = Image.open(path)
    if imagem.mode == "RGB" or imagem.mode == "HSV":
        transformacao_logaritmica_RGB(path,salvar)
    else:
        transformacao_logaritmica_simples(path,salvar)
        

def transformacao_logaritmica_simples(path,salvar):
    img = Image.open(path)
    data = np.array(img)
    c = 255 / numpy.log(1 + numpy.max(numpy.max(data)))
    nova_imagem = (c * numpy.log(1+data)).astype(np.uint8)
    img2 = Image.fromarray(nova_imagem)
    img.close()
    img2.save(salvar)
    img2.close()

def operacao(data):
    ep = 1e-10
    c = 255 / numpy.log(1 + numpy.max(numpy.max(data)))
    valor = (c * numpy.log(1+abs(data)+ep)).astype(np.uint8)   
    
    return valor

def transformacao_logaritmica_RGB(path,salvar):
    imagem = Image.open(path)
    data = np.array(imagem)
    canal_r = operacao(data[:,:,0] )
    canal_g = operacao(data[:,:,1])
    canal_b = operacao(data[:,:,2])
    imagem_transformada_array = np.stack((canal_r, canal_g, canal_b), axis=-1)
    imagem_transformada_array = (imagem_transformada_array / np.max(imagem_transformada_array) * 255).astype(np.uint8)
    imagem_transformada = Image.fromarray(imagem_transformada_array)
    imagem_transformada.save(salvar)
