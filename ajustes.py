from PIL import Image,ImageDraw
import conversao

def ajuste_matiz(img,valor,salvar):
    # imagem = Image.open(img)
    imagem_hsv = conversao.converter_RGB_HSV(img)
    largura = imagem_hsv.width
    altura = imagem_hsv.height
    imagem_nova = Image.new('RGB',(largura,altura))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(altura):
        for coluna in range(largura):
            H,S,V = imagem_hsv.getpixel((coluna,linha))
            H = (H*360/100)+valor
            if H > 360:
                nova_imagem.point((coluna,linha),fill=conversao.HSV_RGB(H-360,S,V))
            elif H < 0:
                nova_imagem.point((coluna,linha),fill=conversao.HSV_RGB(H+360,S,V))
            else:
                nova_imagem.point((coluna,linha),fill=conversao.HSV_RGB(H,S,V))
    imagem_nova.save(salvar)
    imagem_nova.close()

def ajuste_saturacao(img,valor,salvar):
    # imagem = Image.open(img)
    imagem_hsv = conversao.converter_RGB_HSV(img)
    largura = imagem_hsv.width
    altura = imagem_hsv.height
    imagem_nova = Image.new('RGB',(largura,altura))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(altura):
        for coluna in range(largura):
            H,S,V = imagem_hsv.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=conversao.HSV_RGB(H*360/100,S+valor,V))
    imagem_nova.save(salvar)
    imagem_nova.close()
    imagem_hsv.close()

def ajuste_brilho(img,valor,salvar):
    # imagem = Image.open(img)
    imagem_hsv = conversao.converter_RGB_HSV(img)
    largura = imagem_hsv.width
    altura = imagem_hsv.height
    imagem_nova = Image.new('RGB',(largura,altura))
    nova_imagem = ImageDraw.Draw(imagem_nova)
    for linha in range(altura):
        for coluna in range(largura):
            H,S,V = imagem_hsv.getpixel((coluna,linha))
            nova_imagem.point((coluna,linha),fill=conversao.HSV_RGB(H*360/100,S,V+valor))
    imagem_nova.save(salvar)
    imagem_nova.close()
    imagem_hsv.close()


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
    imagem.close()
    imagem_nova.close()


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
    imagem.close()
    imagem_nova.close()


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
    imagem.close()
    imagem_nova.close()