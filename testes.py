
import numpy as np
from PIL import Image
import os
import huffman
import codificacao_preditiva
import wavelet

def compactar_imagem(caminho, saida):
    compressed_img = wavelet.compress(caminho)
    encoded_data = codificacao_preditiva.predictive_coding_encode(compressed_img)
    huffman.compress_array(encoded_data,saida)

def descompactar_imagem(caminho, saida):
    imagem_codificada =huffman.decompress_image(caminho)
    codificacao_preditiva.decodificacao_preditiva(imagem_codificada,saida)

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    while True:
        # try:
            caminho = str(input("Digite o caminho da imagem: "))
            escolha = int(input("Você deseja:\n1 - descompactar\n2 - compactar a imagem:\n"))

            if escolha == 1:
                saida = f'{caminho.split(".")[0]}_saida.bmp'
                descompactar_imagem(caminho,saida)
                print(f'Tamanho da imagem comprimida: {os.path.getsize(caminho)}')
                print(f'Tamanho da imagem descomprimida: {os.path.getsize(saida)}')

            elif escolha == 2:
                saida = f'{caminho.split(".")[0]}.grr'
                compactar_imagem(caminho, saida)
                print(f'Tamanho da imagem original: {os.path.getsize(caminho)}')
                print(f'Tamanho da imagem comprimida: {os.path.getsize(saida)}')
            
        # except (EOFError, KeyboardInterrupt):
        #     print("\nFim do programa.")
        #     break
        # except:
        #     limpar_terminal()
        #     print("Ocorreu um erro inesperado") 