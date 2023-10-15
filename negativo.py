from PIL import Image, ImageDraw
from numpy import asarray;

def inverter(path,salvar):
    imagem = Image.open(path)
    if imagem.mode == "RGB" or imagem.mode == "HSV":
        negativo_RGB(path,salvar)
    else:
        negativo_simples(path,salvar)

def negativo(r,g,b):
    neg_r = 255 - r
    neg_g = 255 - g
    neg_b = 255 - b
    return neg_r,neg_g,neg_b    

def negativo_RGB(img,salvar):
    imagem_original = Image.open(img)
    imagem_cinza = Image.new('RGB',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_cinza)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=negativo(r,g,b))

    imagem_cinza.save(salvar)

def negativo_simples(path,salvar):
    img = Image.open(path)
    data = asarray(img) / 255.0
    data = (1 - data)*255
    img2 = Image.fromarray(data)
    img.close()
    img2.save(salvar)
    img2.close()
