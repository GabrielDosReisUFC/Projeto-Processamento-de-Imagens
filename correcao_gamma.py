from PIL import Image
import numpy as np;
from numpy import asarray;

def gamma(path,gamma,salvar):
    imagem = Image.open(path)
    if imagem.mode == "RGB" or imagem.mode == "HSV":
        return gamma_RGB(path,gamma,salvar)
    else:
        return gamma_simples(path,gamma,salvar)

def gamma_simples(path,gamma,salvar):
    img = Image.open(path)
    data = asarray(img)
    try:
        nova_imagem = np.power(data / 255.0, gamma) * 255.0
        img2 = Image.fromarray(nova_imagem)
        img2.save(salvar)
        img2.close()
    except:        
        img.close()
        return False
    img.close()
    return True

def operacao(data,gamma):
    return np.power(data / 255.0, gamma) * 255.0

def gamma_RGB(path,gamma,salvar):
    imagem = Image.open(path)
    data = np.array(imagem)
    canal_r = operacao(data[:,:,0],gamma)
    canal_g = operacao(data[:,:,1],gamma)
    canal_b = operacao(data[:,:,2],gamma)
    try:
        imagem_transformada_array = np.stack((canal_r, canal_g, canal_b), axis=-1)
        imagem_transformada_array = (imagem_transformada_array / np.max(imagem_transformada_array) * 255).astype(np.uint8)
        imagem_transformada = Image.fromarray(imagem_transformada_array)
        imagem_transformada.save(salvar)
        imagem_transformada.close()
    except:
        return False
    imagem.close()
    return True
