import rgb2hsv
from PIL import Image,ImageDraw
import numpy as np

def ajuste_matiz(img,valor,salvar):
    imagem = Image.open(img)
    imagem_hsv = rgb2hsv.rgb2hsv(imagem)
    imagem_nova = Image.new('RGB',(imagem_hsv.width,imagem_hsv.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem_hsv.height):
        for coluna in range(imagem_hsv.width):
            H,S,V = imagem_hsv.getpixel((coluna,linha))
            H = (H+valor)*360/100 
            nova_imagem.point((coluna,linha),fill=rgb2hsv.hsv2rgb(H,S,V))
    imagem_nova.save(salvar)

def ajuste_saturacao(img,valor,salvar):
    imagem = Image.open(img)
    imagem_hsv = rgb2hsv.rgb2hsv(imagem)
    imagem_nova = Image.new('RGB',(imagem_hsv.width,imagem_hsv.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem_hsv.height):
        for coluna in range(imagem_hsv.width):
            H,S,V = imagem_hsv.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=rgb2hsv.hsv2rgb(H,S+valor,V))
    imagem_nova.save(salvar)


def ajuste_brilho(img,valor,salvar):
    imagem = Image.open(img)
    imagem_hsv = rgb2hsv.rgb2hsv(imagem)
    imagem_nova = Image.new('RGB',(imagem_hsv.width,imagem_hsv.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem_hsv.height):
        for coluna in range(imagem_hsv.width):
            H,S,V = imagem_hsv.getpixel((coluna,linha))
            if V+valor <=0:
                nova_imagem.point((coluna,linha),fill=rgb2hsv.hsv2rgb(H,S,0))
            elif V+valor >= 100:
                nova_imagem.point((coluna,linha),fill=rgb2hsv.hsv2rgb(H,S,100))
            else:
                nova_imagem.point((coluna,linha),fill=rgb2hsv.hsv2rgb(H,S,V+valor))
    imagem_nova.save(salvar)

def ajuste_R(img,valor,salvar):
    imagem = Image.open(img)
    imagem_nova = Image.new('RGB',(imagem.width,imagem.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem.height):
        for coluna in range(imagem.width):
            R,G,B = imagem.getpixel((coluna,linha))
            if R+valor <=0:
                nova_imagem.point((coluna,linha),fill=(0,G,B))
            elif R+valor >= 255:
                nova_imagem.point((coluna,linha),fill=(255,G,B))
            else:
                nova_imagem.point((coluna,linha),fill=(R+valor,G,B))
    imagem_nova.save(salvar)


def ajuste_G(img,valor,salvar):
    imagem = Image.open(img)
    imagem_nova = Image.new('RGB',(imagem.width,imagem.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem.height):
        for coluna in range(imagem.width):
            R,G,B = imagem.getpixel((coluna,linha))
            if G+valor <=0:
                nova_imagem.point((coluna,linha),fill=(R,0,B))
            elif G+valor >= 255:
                nova_imagem.point((coluna,linha),fill=(R,255,B))
            else:
                nova_imagem.point((coluna,linha),fill=(R,G+valor,B))
    imagem_nova.save(salvar)


def ajuste_B(img,valor,salvar):
    imagem = Image.open(img)
    imagem_nova = Image.new('RGB',(imagem.width,imagem.height))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(imagem.height):
        for coluna in range(imagem.width):
            R,G,B = imagem.getpixel((coluna,linha))
            if B+valor <=0:

                nova_imagem.point((coluna,linha),fill=(R,G,0))
            elif B+valor >= 255:

                nova_imagem.point((coluna,linha),fill=(R,G,255))
            else:
                nova_imagem.point((coluna,linha),fill=(R,G,B+valor))
    imagem_nova.save(salvar)
