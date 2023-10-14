from PIL import Image, ImageFilter
import numpy as np
import cv2

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
    

# Carrega a imagem com Pillow
# image = Image.open('sol.tif')
# sorbel(image)
# imga2 = cv2.imread('robo.tif')
# img1 = image/np.max(np.max(image))
# img_normalizada = Image.fromarray(img1)
# laplaciano(image)
# kernel = np.array([[1, 1, 1], [1, 1, 1,], [1, 1, 1]])
# convoluca_mediana(img_normalizada, 3)
# out = cv2.medianBlur(imga2, 3)
# cv2.imshow('imagem',out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# imagem_suavizada = image.filter(ImageFilter.Kernel(size=(5,5), kernel=kernel2.flatten(),scale=1/25))
# convolucao(img_normalizada, kernel)
# imagem_suavizada.show()
# high_bost(image)