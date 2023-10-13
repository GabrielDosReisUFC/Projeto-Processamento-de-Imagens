from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import retornarPath
import multiprocessing
import numpy as np
from PIL import Image, ImageTk

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
    print(imagem_original.width,imagem_original.height)
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