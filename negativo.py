from PIL import Image,ImageDraw
import numpy as np

def inverter(path,salvar):
    imagem = Image.open(path)
    if imagem.mode == "RGB" or imagem.mode == "HSV":
        negativo_RGB(path,salvar)
    else:
        negativo_simples(path,salvar)

def negativo_simples(path,salvar):
    img = Image.open(path)
    data = np.asarray(img) / 255.0
    data = (1 - data)*255
    img2 = Image.fromarray(data)
    img.close()
    img2.save(salvar)

def operacao(r,g,b):
    return 255 - r, 255-g, 255-b

def negativo_RGB(img,salvar):
    imagem_original = Image.open(img)
    imagem_cinza = Image.new('RGB',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_cinza)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=operacao(r,g,b))

    imagem_cinza.save(salvar)
