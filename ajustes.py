import conversao
from PIL import Image,ImageDraw
import numpy as np

def ajuste_matiz(img,valor):
    imagem_hsv = conversao.converter_RGB_HSV(img)
    imagem_nova = Image.new('RGB',(imagem_hsv.width,imagem_hsv.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem_hsv.height):
        for coluna in range(imagem_hsv.width):
            H,S,V = imagem_hsv.getpixel((linha,coluna))
            H = H * 360/100 + valor
            nova_imagem.point((linha,coluna),fill=conversao.HSV_RGB(H,S,V))
    imagem_nova.show()
    # return imagem_rgb
# ajuste_matiz("imagem_modificada.PNG",90)

def ajuste_saturacao(img,valor):
    imagem_hsv = conversao.converter_RGB_HSV(img)
    imagem_nova = Image.new('RGB',(imagem_hsv.width,imagem_hsv.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem_hsv.height):
        for coluna in range(imagem_hsv.width):
            H,S,V = imagem_hsv.getpixel((linha,coluna))
            nova_imagem.point((linha,coluna),fill=conversao.HSV_RGB(H,S+valor,V))
    imagem_nova.show()

# ajuste_saturacao("imagem_modificada.PNG",100)

def ajuste_brilho(img,valor):
    imagem_hsv = conversao.converter_RGB_HSV(img)
    imagem_nova = Image.new('RGB',(imagem_hsv.width,imagem_hsv.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem_hsv.height):
        for coluna in range(imagem_hsv.width):
            H,S,V = imagem_hsv.getpixel((linha,coluna))
            # print(V)
            if V+valor <=0:
                # print(conversao.HSV_RGB(H,S,0))
                nova_imagem.point((linha,coluna),fill=conversao.HSV_RGB(H,S,0))
            elif V+valor >= 100:
                # print(conversao.HSV_RGB(H,S,0))
                nova_imagem.point((linha,coluna),fill=conversao.HSV_RGB(H,S,100))
            else:
                nova_imagem.point((linha,coluna),fill=conversao.HSV_RGB(H,S,V+valor))
    imagem_nova.show()

# ajuste_brilho("imagem_modificada.PNG",100)
