from PIL import Image 
import numpy as np

def carregar_imagem(caminho):
    imagem = Image.open(caminho)
    array_imagem = np.array(imagem, dtype=np.int16)
    return array_imagem,imagem.size

def predictive_coding_encode(image,tam):
    x,y = tam
    imagem_copia = np.array(image, dtype=np.int16)
    for i in range(y):  
        for j in range(x):
            if i == 0 and j == 0:
                # Para o primeiro pixel, a distância é o próprio valor
                imagem_copia[i, j] = image[i, j] + 255
            elif i == 0:
                # Para a primeira coluna, a distância é a diferença para o pixel acima
                imagem_copia[i, j] = image[i, j] - image[i, j- 1] + 255
            elif j == 0: 
                # Para a primeira linha, a distância é a diferença para o pixel à esquerda
                imagem_copia[i, j] = image[i, j] - image[i - 1, j] + 255
            else:
                # Para outros pixels, a distância é a média das diferenças dos pixels acima e à esquerda
                imagem_copia[i, j] = image[i, j] - (image[i - 1, j] + image[i, j - 1]) // 2 + 255
        
    return imagem_copia 


def decodificacao_preditiva(imagem_codificada,saida):
    largura, altura, canais = imagem_codificada.shape
    imagem_decodificada = np.zeros((largura, altura, canais), dtype=np.int16)
    for i in range(largura):
        for j in range(altura):
            if i == 0 and j == 0:
                # Para o primeiro pixel, o valor é a própria distância
                imagem_decodificada[i, j] = imagem_codificada[i, j] - 255
            elif i == 0:
                # Para a primeira coluna, o valor é a soma do valor acima e a distância
                imagem_decodificada[i, j] = imagem_decodificada[i, j - 1] + imagem_codificada[i, j]  - 255
            elif j == 0:
                # Para a primeira linha, o valor é a soma do valor à esquerda e a distância
                imagem_decodificada[i, j] = imagem_decodificada[i - 1, j] + imagem_codificada[i, j]  - 255
            else:
                # Para outros pixels, o valor é a soma da média dos valores acima e à esquerda e a distância
                imagem_decodificada[i, j] = imagem_codificada[i, j] - 255 + (imagem_decodificada[i - 1, j] + imagem_decodificada[i, j - 1]) // 2 
    imagem_decodificada = imagem_decodificada.astype(np.uint8)
    
    img = Image.fromarray(imagem_decodificada)
    img .save(saida)
