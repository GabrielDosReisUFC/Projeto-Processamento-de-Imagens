from PIL import Image
import numpy as np
import math

def convolucao(img, kernel,salvar):
    image = Image.open(img)
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    for x in range(0, width):
        for y in range(0, height):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      accumulator += pixel_value * kernel[i + padding, j + padding]
            nova_imga[y][x] = accumulator
    imga = Image.fromarray(nova_imga/np.max(np.max(nova_imga))* 255)
    imga.close()

def convolucao_media(img,tam,salvar):
    matrix = np.ones((tam,tam),dtype=int) * pow(tam,2)
    convolucao(img,matrix,salvar)

def convoluca_mediana(path, tam,salvar):
    image = Image.open(path)
    width, height = image.size
    padding = tam // 2
    nova_imga = np.zeros((height,width))
    for x in range(0, width):
        for y in range(0, height):
            auxiliar = []
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      auxiliar.append(pixel_value)
                    else:
                        auxiliar.append(0)
            auxiliar.sort()
            nova_imga[y][x] = auxiliar[int((tam*tam+1)/2)-1]
    imga = Image.fromarray(nova_imga/np.max(np.max(nova_imga))* 255)
    imga.save(salvar)
    imga.close()

def laplaciano(img,salvar):
    image = Image.open(img)
    kernel = np.array([[0, 1, 0], [1, -4, 1,], [0, 1, 0]])
     
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    for x in range(0, width):
        for y in range(0, height):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      accumulator += pixel_value * kernel[i + padding, j + padding] 
            nova_imga[y][x] = abs(accumulator)
    imga = Image.fromarray(nova_imga)
    imga.save(salvar)
    imga.close()

def gauss(img,num):
    image = Image.open(img)
    if num == 1: kernel = np.array([[1, 2, 1], [2, 4, 2,], [1, 2, 1]]) * 1/16
    else : kernel = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4],[1, 4, 6, 4, 1]]) *1/256
     
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    for x in range(0, width):
        for y in range(0, height):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      accumulator += pixel_value * kernel[i + padding, j + padding]
            nova_imga[y][x] = accumulator
    
    nova_imga = nova_imga/np.max(np.max(nova_imga)) *255
    imagem_final = Image.fromarray(nova_imga)
    return nova_imga
 
def high_boost(imagem,salvar):
    img = Image.open(imagem)
    array = np.array(img)
    img_borrada = gauss(imagem,1)
    img_2 = array - img_borrada
    img_2 = img_2/np.max(np.max(img_2))* 255
    img_3 = img + 1.2*img_2
    img_final = Image.fromarray(img_3/np.max(np.max(img_3))* 255)
    img_final.save(salvar)

def sobel_x(img):
    image = Image.open(img)
    kernel = np.array([[-1, 0, 1], [-2, 0, 2,], [-1, 0, 1]])
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    for x in range(0, width):
        for y in range(0, height):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      accumulator += pixel_value * kernel[i + padding, j + padding]
            nova_imga[y][x] = accumulator

    return nova_imga

def sobel_y(img):
    image = Image.open(img)
    kernel = np.array([[-1, -2, -1], [0, 0, 0,], [1, 2, 1]])
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    for x in range(0, width):
        for y in range(0, height):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      accumulator += pixel_value * kernel[i + padding, j + padding]
            nova_imga[y][x] = accumulator

    return nova_imga

def sobel(img,salvar):
    x = sobel_x(img)
    y = sobel_y(img)
    img_final = abs(x) + abs(y)
    nova_imga = Image.fromarray(img_final/np.max(np.max(img_final))* 255)
    nova_imga.save(salvar)

def convolucao_rgb(img, kernel,salvar):
    image = Image.open(img)
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    imagem_suavizada = Image.new("RGB", image.size)
    pixels_suavizados = imagem_suavizada.load()
    for x in range(0, width):
        for y in range(0, height):
            accumulator_r = 0
            accumulator_g = 0
            accumulator_b = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      r,g,b = image.getpixel((x + i, y + j))
                      accumulator_r += math.floor(r * kernel[i + padding, j + padding])
                      accumulator_g += math.floor(g * kernel[i + padding, j + padding])
                      accumulator_b += math.floor(b * kernel[i + padding, j + padding])
            pixels_suavizados[x,y] = (accumulator_r,accumulator_g,accumulator_b)

    imagem_suavizada.save(salvar)

def suavizacao_rgb(img,salvar):
    kernel = np.array([[1, 1, 1], [1, 1, 1,], [1, 1, 1]])*1/9
    convolucao_rgb(img,kernel,salvar)

def agucamento_rgb(img,salvar):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1,], [-1, -1, -1]])
    convolucao_rgb(img,kernel,salvar)
