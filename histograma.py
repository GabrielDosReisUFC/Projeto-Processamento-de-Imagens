from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from rgb2hsv import rgb2hsv
from rgb2hsv import hsv2rgb
from PIL import Image

def contagem_de_pixels(height, width, dados_imagem):
    contagem_pixel = [0] * 256
    for linha in range(height):
        for coluna in range(width):
            i = round(dados_imagem[linha,coluna])
            contagem_pixel[i] += 1
    return contagem_pixel

def histograma(file_path):
    imagem_original = Image.open(file_path)  
    #imagem_original.save(file_path)
    dados_imagem = np.array(imagem_original)
    # pixel_total = imagem_original.height * imagem_original.width

    contagem_pixel = contagem_de_pixels(imagem_original.height, imagem_original.width, dados_imagem) 

    plt.plot(range(0,256),contagem_pixel)
    plt.show()

def histograma_equalizado(file_path,salvar):
    
    imagem_original = Image.open(file_path)  
    #imagem_original.save(file_path)
    dados_imagem = np.array(imagem_original)
    pixel_total = imagem_original.height * imagem_original.width
    
    contagem_pixel = contagem_de_pixels(imagem_original.height, imagem_original.width, dados_imagem) 
    acumulado = [0] * 256
    cont = 0
    
    for i in contagem_pixel:
        acumulado[cont] = acumulado[cont-1]+i
        cont += 1

    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            
            i = round(dados_imagem[linha,coluna])
            dados_imagem[linha,coluna] = round(255*acumulado[i]/pixel_total)
    
    img2 = Image.fromarray(dados_imagem)
    imagem_original.close()
    img2.save(salvar)
    contagem_equalizada = contagem_de_pixels(img2.height,img2.width,np.array(img2))
    img2.close()
    return contagem_equalizada

def histograma_intensidade(img):
    imagem = rgb2hsv.rgb2hsv(img)
    contagem_pixel_intensiade = [0]*101
    for linha in range(imagem.height):
        for coluna in range(imagem.width):
            H,S,I = imagem.getpixel((coluna,linha))
            contagem_pixel_intensiade[I] += 1

    # plt.plot(range(0,101),contagem_pixel_intensiade)
    # plt.show()
    return contagem_pixel_intensiade

def histograma_rgb(file_path):
    imagem_original = Image.open(file_path)  
    contagem_pixel_r = [0] * 256
    contagem_pixel_g = [0] * 256
    contagem_pixel_b = [0] * 256

    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            r,g,b = imagem_original.getpixel((coluna,linha))
            contagem_pixel_r[r] += 1
            contagem_pixel_g[g] += 1
            contagem_pixel_b[b] += 1

    contagem_I = histograma_intensidade(file_path)

    plt.figure(figsize=(12,4))
    plt.subplot(141)
    plt.title('Histograma de R')
    plt.xlabel('Pixels')
    plt.ylabel('intensidade')
    plt.plot(range(0,256),contagem_pixel_r)
    
    plt.subplot(142)
    plt.title('Histograma de G')
    plt.xlabel('Pixels')
    plt.ylabel('intensidade')
    plt.plot(range(0,256),contagem_pixel_g)

    plt.subplot(143)
    plt.title('Histograma de B')
    plt.xlabel('Pixels')
    plt.ylabel('intensidade')
    plt.plot(range(0,256),contagem_pixel_b)
    
    plt.subplot(144)
    plt.title('Histograma de I')
    plt.xlabel('Pixels')
    plt.ylabel('intensidade')
    plt.plot(range(0,101),contagem_I)

    plt.tight_layout()
    plt.show()

# histograma_rgb("mulher.tif")
# histograma_intensidade("mulher.tif")

def equalizar_intensidade(img,salvar):
    imagem = rgb2hsv.rgb2hsv(img)    
    intensidade = np.array(imagem)[:,:,2]
    contagem_pixel = histograma_intensidade(img) 
    acumulado = np.zeros(101,dtype=int)
    acumulado[0] = contagem_pixel[0]
    for i in range(1,101):
        acumulado[i] = acumulado[i-1]+contagem_pixel[i]

    acumulado_normalizado = (acumulado*100/acumulado[-1]).astype(int)
    intensidade_normalizada = acumulado_normalizado[intensidade]

    imagem_equalizada = imagem.copy()
    imagem_equalizada = Image.fromarray(np.array(imagem_equalizada), "HSV")
    imagem_equalizada = rgb2hsv.hsv2rgb(imagem_equalizada)
    imagem_equalizada = np.array(imagem_equalizada)
    imagem_equalizada[:,:,2] = intensidade_normalizada * 255 / 100

    imagem_equalizada = Image.fromarray(imagem_equalizada, "RGB")
    imagem_equalizada.save(salvar)

    return histograma_intensidade(salvar) 

