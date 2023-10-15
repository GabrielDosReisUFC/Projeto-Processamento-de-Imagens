import math
from PIL import Image,ImageDraw
import numpy as np

def RGB_HSV(R,G,B):
    H = 0 ; S = 0 ; V = 0
    R = R/ 255; G = G/ 255; B = B/ 255; 
    C_max = max(R,G,B)
    C_min = min(R,G,B)
    delta = C_max - C_min
    
    if delta == 0:
        pass
    elif C_max == R:
        H = 60 * (((G-B)/delta)%6)
    elif C_max == G:
        H = 60 * ((B-R)/delta+2)
    elif C_max == B:
        H = 60 * ((R-G)/delta+4)

    if C_max == 0:
        S = 0
    else:
        S = delta/C_max * 100

    V = C_max * 100
    H = H * 100 / 360
    # S = S * 255 / 100
    # V = V * 255 / 100
    return math.floor(H),math.floor(S),math.floor(V)

def converter_RGB_HSV(img):
    imagem_original = Image.open(img)
    pixels = imagem_original.load()
    imagem_hsv = Image.new('HSV',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_hsv)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=RGB_HSV(r,g,b))

    return imagem_hsv

    # nao eh possivel salvar
    # imagem_hsv.save("foguette.png")
    
# converter_RGB_HSV("mulher.tif")
def HSV_RGB(H,S,V):
    S = S/100
    V = V/100
    R = 0; G = 0; B = 0
    C = V * S
    X = C * (1-abs((H/60)%2-1))
    m = V-C

    if H < 60:
        R = C
        G = X
        B = 0
    elif H < 120:
        R = X
        G = C
        B = 0
    elif H < 180:
        R = 0
        G = C
        B = X
    elif H < 240:
        R = 0
        G = X
        B = C
    elif H < 300:
        R = X
        G = 0
        B = C
    else:
        R = C
        G = 0
        B = X

    R = (R+m)*255
    G = (G+m)*255
    B = (B+m)*255

    return math.floor(R),math.floor(G),math.floor(B)

def converter_HSV_RGB(img):
    try:
        imagem_original = Image.open(img)
    except:
        imagem_original = img
    pixels = imagem_original.load()
    imagem_rgb = Image.new('RGB',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_rgb)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            H,S,V = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=HSV_RGB(H,S,V))

    return imagem_rgb

    # nao eh possivel salvar
    # imagem_hsv.save("foguette.png")

def converter_escala_cinza(img,salvar):
    imagem_original = Image.open(img)
    imagem_cinza = Image.new('L',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_cinza)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=((r+g+b)//3))

    imagem_cinza.save(salvar)


# def escala_cinza_ponderada(r,g,b,peso1,peso2,peso3):
#     print(r,g,b)
#     print(peso1)
#     print(peso2)
#     print(peso3)
#     cinza = 
#     print(cinza)
#     math.floor(cinza)
#     print(cinza)
#     return cinza

def converter_escala_cinza_ponderada(img,salvar,peso1,peso2,peso3):
    imagem_original = Image.open(img)
    imagem_cinza = Image.new('L',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_cinza)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=((peso1*r+peso2*g+peso3*b)//(peso1+peso2+peso3)))

    imagem_cinza.save(salvar)

def negativo(r,g,b):
    neg_r = 255 - r
    neg_g = 255 - g
    neg_b = 255 - b
    return neg_r,neg_g,neg_b

def converter_negativo(img,salvar):
    imagem_original = Image.open(img)
    imagem_cinza = Image.new('RGB',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_cinza)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=negativo(r,g,b))

    imagem_cinza.save(salvar)

def serpia(r,g,b):
    serpia_r = (0.393 * r + 0.769 * g + 0.189 * b)
    serpia_g = (0.349 * r + 0.686 * g + 0.168 * b)
    serpia_b = (0.272 * r + 0.534 * g + 0.131 * b)

    return math.floor(serpia_r),math.floor(serpia_g),math.floor(serpia_b)

def converter_serpia(img,salvar):
    imagem_original = Image.open(img)
    imagem_cinza = Image.new('RGB',(imagem_original.width,imagem_original.height))
    nova_imagem = ImageDraw.Draw(imagem_cinza)
    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=serpia(r,g,b))

    imagem_cinza.save(salvar)
# converter_serpia("mulher.tif","serpia.tif")