from PIL import Image, ImageDraw
import numpy as np
import cv2
import math
# Função para realizar a convolução entre a imagem e o kernel

def convolucao(img, kernel,salvar):
    image = Image.open(img)
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    # Cria uma nova imagem vazia para armazenar o resultado
    for x in range(0, width):
        # auxiliar = []
        for y in range(0, height):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      accumulator += pixel_value * kernel[i + padding, j + padding]
            # auxiliar.append(accumulator)
            nova_imga[y][x] = accumulator
    # return result
    imga = Image.fromarray(nova_imga/np.max(np.max(nova_imga))* 255)
    imga.save(salvar)
    # imga.show()
    imga.close()

def convolicao_media(img,tam,salvar):
    matrix = np.ones((tam,tam),dtype=int) * pow(tam,2)
    convolucao(img,matrix,salvar)

def convoluca_mediana(path, tam,salvar):
    image = Image.open(path)
    width, height = image.size
    padding = tam // 2
    nova_imga = np.zeros((height,width))
    # Cria uma nova imagem vazia para armazenar o resultado
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
    # imga.show()
    imga.save(salvar)
    imga.close()
    
def laplaciano(img,salvar):
    image = Image.open(img)
    kernel = np.array([[0, 1, 0], [1, -4, 1,], [0, 1, 0]])
    # kernel2 = np.array([[1, 1, 1], [1, -8, 1,], [1, 1, 1]])
    # kernel3 = kernel*(-1)
    # kernel4 = kernel2*(-1)
     
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    # Cria uma nova imagem vazia para armazenar o resultado
    for x in range(0, width):
        for y in range(0, height):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      pixel_value = image.getpixel((x + i, y + j))
                      accumulator += pixel_value * kernel[i + padding, j + padding] *255
            nova_imga[y][x] = accumulator
    imga = Image.fromarray(nova_imga/np.max(np.max(nova_imga))* 255)
    imga2 = Image.fromarray(nova_imga/np.max(np.max(nova_imga))* 255 +image)
    imga.close()
    # imga.show()
    imga2.save(salvar)
    # imga2.show()
    imga2.close()

def gauss(img,num):
    image = Image.open(img)
    if num == 1: kernel = np.array([[1, 2, 1], [2, 4, 2,], [1, 2, 1]]) * 1/16
    else : kernel = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4],[1, 4, 6, 4, 1]]) *1/256
    # kernel3 = kernel*(-1)
    
     
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    nova_imga = np.zeros((height,width))
    # Cria uma nova imagem vazia para armazenar o resultado
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
 
    
def high_bost(imagem,salvar):
    img = Image.open(imagem)
    array = np.array(img)
    img_borrada = gauss(img,1)
    img_2 = array - img_borrada
    img_3 = img + 1.2*img_2
    img_final = Image.fromarray(img_3/np.max(np.max(img_3))* 255)
    # img_final.show()
    img_final.save(salvar)
    img_final.close()

def sorbel_x(image):
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
    imga2 = Image.fromarray(nova_imga/np.max(np.max(nova_imga))* 255 +image)
    # imga2.show()
    return nova_imga

def sorbel_y(img):
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
    imga2 = Image.fromarray(nova_imga/np.max(np.max(nova_imga))* 255 +image)
    # imga2.show()
    return nova_imga
    
def sorbel(img,salvar):
    x = sorbel_x(img)
    y = sorbel_y(img)
    img_final = abs(x) + abs(y)
    nova_imga = Image.fromarray(img_final/np.max(np.max(img_final))* 255)
    # nova_imga.show()
    nova_imga.save(salvar)
    
def convolucao_rgb(img, kernel):
    image = Image.open(img)
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    imagem_suavizada = Image.new("RGB", image.size)
    pixels_suavizados = imagem_suavizada.load()
    # Cria uma nova imagem vazia para armazenar o resultado
    for x in range(0, width):
        # auxiliar = []
        for y in range(0, height):
            accumulator_r = 0
            accumulator_g = 0
            accumulator_b = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    if (x + i >= 0 and x + i < width) and (y + j >= 0 and y + j < height):
                      r,g,b = image.getpixel((x + i, y + j))
                      accumulator_r += math.floor(r * kernel[i + padding, j + padding])
                      accumulator_g += math.floor(r * kernel[i + padding, j + padding])
                      accumulator_b += math.floor(r * kernel[i + padding, j + padding])
            pixels_suavizados[x,y] = (accumulator_r,accumulator_g,accumulator_b)

    # imga_array = np.array(imagem_suavizada)
    # print(imga_array)
    # imga_normalizada = Image.fromarray(imga_array/np.max(np.max(np.max(imga_array)))* 255).astype(np.uint8)
    # imga = Image.fromarray(imga_normalizada)
    # imga.show()
    imagem_suavizada.show()

def suavizacao_rgb(img):
    kernel = np.array([[1, 1, 1], [1, 1, 1,], [1, 1, 1]])*1/9
    convolucao_rgb(img,kernel)

def agucamento_rgb(img):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1,], [-1, -1, -1]])
    convolucao_rgb(img,kernel)

