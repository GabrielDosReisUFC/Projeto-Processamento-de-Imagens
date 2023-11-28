import numpy as np
from PIL import Image
import os
import huffman
import codificacao_preditiva
import wavelet

def compactar_imagem(caminho, saida):
    compressed_img = wavelet.compress(caminho)
    array ,tam = codificacao_preditiva.carregar_imagem(compressed_img)
    encoded_data = codificacao_preditiva.predictive_coding_encode(array,tam)
    huffman.compress_array(encoded_data,saida)

def descompactar_imagem(caminho, saida):
    imagem_codificada =huffman.decompress_image(caminho)
    codificacao_preditiva.decodificacao_preditiva(imagem_codificada,saida)

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def salvar_imagem_personalizada(nome_do_arquivo, dados_imagem):
    with open(nome_do_arquivo, 'wb') as arquivo:
        np.save(arquivo, dados_imagem)

def carregar_imagem_personalizada(nome_do_arquivo):
    with open(nome_do_arquivo, 'rb') as arquivo:
        dados_imagem = np.load(arquivo)

    # Criar uma imagem PIL a partir dos dados
    return Image.fromarray(dados_imagem)

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