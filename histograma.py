from PIL import Image
import matplotlib.pyplot as plt
import retornarPath
import threading

def contar_hist(height, width, dados_imagem):
    contagem_pixel = [0] * 256
    for linha in range(height):
        for coluna in range(width):
            i = round(dados_imagem[coluna, linha])
            contagem_pixel[i] += 1
    return contagem_pixel

def hist(file_path):
    imagem_original = Image.open(file_path)  
    dados_imagem = imagem_original.load()
    pixel_total = imagem_original.height * imagem_original.width
    
    contagem_pixel = contar_hist(imagem_original.height, imagem_original.width, dados_imagem)     
    
    return imagem_original, pixel_total, dados_imagem, pixel_total, contagem_pixel

def plotar(array):
    plt.plot(range(0,256),array)
    plt.show()

def histograma(file_path):
    imagem_original, pixel_total, dados_imagem, pixel_total, contagem_pixel = hist(file_path)

    plotar(contagem_pixel)

def histograma_equalizado(file_path):
    imagem_original, pixel_total, dados_imagem, pixel_total, contagem_pixel = hist(file_path)
    acumulado = [0] * 256
    cont = 0
    
    # hits acumulado
    for i in contagem_pixel:
        acumulado[cont] = acumulado[cont-1]+i
        cont += 1

    for linha in range(imagem_original.height):
        for coluna in range(imagem_original.width):
            i = round(dados_imagem[coluna, linha])
            dados_imagem[coluna, linha] = round(255*acumulado[i]/pixel_total)
    
    nova_contagem = contar_hist(imagem_original.height, imagem_original.width, dados_imagem)

    thread = threading.Thread(target=plotar, args=(nova_contagem,))
    thread.start()

    return retornarPath.path(file_path,imagem_original)