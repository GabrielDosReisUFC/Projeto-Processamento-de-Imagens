from PIL import Image
import numpy as np
from collections import Counter

# Ordena a quantidade de ocorrencia da intensidade
def contar_numeros(image):
    pixels = image.flatten()
    counts = Counter(pixels).items()
    return sorted(counts, key=lambda x: x[::-1])

# Constroe árvore de cima para baixo 
def construir_arvore(counts):
    nodes = [entry[::-1] for entry in counts] # Reverter cada tupla (símbolo, contagem)
    while len(nodes) > 1:
        leastTwo = tuple(nodes[0:2])  # Obter os 2 para combinar
        theRest = nodes[2:] # Todos os outros
        combFreq = leastTwo[0][0] + leastTwo[1][0] # Frequência do ponto de ramificação
        nodes = theRest + [(combFreq, leastTwo)] # Adicionar ponto de ramificação ao final
        nodes.sort(key=lambda x: x[0])  # Usando x[0] para ordenar pela frequência
    return nodes[0] # Retornar a única árvore dentro da lista

# Função usada para retornar somente os simbolos ordenados por frequencia da arvore
def podar(tree):
    p = tree[1]
    if type(p) is tuple:
        return (podar(p[0]), podar(p[1]))
    return p

def descer_arvore(codes, node, pat):
    if type(node) == tuple: # Ponto de ramificação.
        descer_arvore(codes, node[0], pat + [0]) # Faça o ramo esquerdo.
        descer_arvore(codes, node[1], pat + [1]) # Em seguida, faça o ramo direito.
    else:
        codes[node] = pat # Uma folha

def criar_dicionario(tree): # Faz a inicialização do dicionário que vai ser usado para acessar os códigos na arvore
    codes = {}
    descer_arvore(codes, tree, [])
    return codes

def binario_lista(n): # Converter um inteiro em na menor lista de bits
    return [n] if (n <= 1) else binario_lista(n >> 1) + [n & 1]

def lista_binario(bits):
    result = 0 
    for bit in bits: # Converter uma lista de bits em um inteiro
        result = (result << 1) | bit
    return result

def preencher(bits, n):
    # Preenche a lista de bits até que ela tenha um total de n digitos
    assert(n >= len(bits))
    return ([0] * (n - len(bits)) + bits)

class OutputBitStream(object):
    # Inicializa um arquivo que será usado para escrever
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'wb')
        self.bytes_written = 0
        self.buffer = []

    # Usado para escerver um bit no buffer
    def write_bit(self, value):
        self.write_bits([value])

    # Se o buffer for maior que 8, escrevemos os bits no arquivo
    def write_bits(self, values):
        self.buffer += values
        while len(self.buffer) >= 8:
            self._save_byte()

    def flush(self):
        if len(self.buffer) > 0:  # Adiciona zeros para completar o byte e depois o escreve
            self.buffer += [0] * (8 - len(self.buffer))
            self._save_byte()
        assert(len(self.buffer) == 0)
    
    # Sava as informações no arquivo
    def _save_byte(self):
        bits = self.buffer[:8]
        self.buffer[:] = self.buffer[8:]

        byte_value = lista_binario(bits)
        if 0 <= byte_value <= 255:
            self.file.write(bytes([byte_value]))
            self.bytes_written += 1
        else:
            raise ValueError(f"Invalid byte value: {byte_value}")

    # garante que tudo seja escrito no arquivo antes de fechá-lo
    def close(self):
        self.flush()
        self.file.close()

def codificar_cabecalho(image, bitstream):
    height_bits = preencher(binario_lista(image.shape[0]), 16)
    bitstream.write_bits(height_bits)
    width_bits = preencher(binario_lista(image.shape[1]), 16)
    bitstream.write_bits(width_bits)

def codificar_arvore(tree, bitstream):
    if type(tree) == tuple:
        bitstream.write_bit(0)
        codificar_arvore(tree[0], bitstream)
        codificar_arvore(tree[1], bitstream)
    else:
        bitstream.write_bit(1)
        symbol_bits = preencher(binario_lista(tree), 16)
        bitstream.write_bits(symbol_bits)

def codificar_pixels(image, codes, bitstream):
    pixels = image.flatten()
    for value in pixels:
        bitstream.write_bits(codes[value])

def compressed_size(counts, codes):
    header_size = 2 * 16 

    tree_size = len(counts) * (1 + 16)  
    if tree_size % 8 > 0:
        tree_size += 8 - (tree_size % 8)

    pixels_size = sum([count * len(codes[symbol]) for symbol, count in counts])
    if pixels_size % 8 > 0:
        pixels_size += 8 - (pixels_size % 8)

    return (header_size + tree_size + pixels_size) / 8

def compress_array(array, out_file_name):
    counts = contar_numeros(array)
    tree = construir_arvore(counts)
    trimmed_tree = podar(tree)
    codes = criar_dicionario(trimmed_tree)
    stream = OutputBitStream(out_file_name)
    codificar_cabecalho(array, stream)
    stream.flush() 
    codificar_arvore(trimmed_tree, stream)
    stream.flush()
    codificar_pixels(array, codes, stream)
    stream.close()

# Ler bits de um arquivo
class InputBitStream(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'rb')
        self.bytes_read = 0
        self.buffer = []

    def read_bit(self):
        return self.read_bits(1)[0]

    def read_bits(self, count):
        while len(self.buffer) < count:
            self._load_byte()
        result = self.buffer[:count]
        self.buffer[:] = self.buffer[count:]
        return result

    def flush(self):
        assert(not any(self.buffer))
        self.buffer[:] = []

    def _load_byte(self):
        value = ord(self.file.read(1))
        self.buffer += preencher(binario_lista(value), 8)
        self.bytes_read += 1

    def close(self):
        self.file.close()

def decodificar_cabecalho(bitstream):
    height = lista_binario(bitstream.read_bits(16))
    width = lista_binario(bitstream.read_bits(16))
    return (height, width)

def decodificar_arvore(bitstream):
    flag = bitstream.read_bits(1)[0]
    if flag == 1:
        return np.uint16(lista_binario(bitstream.read_bits(16)))
    left = decodificar_arvore(bitstream)
    right = decodificar_arvore(bitstream)
    return (left, right)

def decodificar_valor(tree, bitstream):
    bit = bitstream.read_bits(1)[0]
    node = tree[bit]
    if type(node) == tuple:
        return decodificar_valor(node, bitstream)
    return np.uint16(node)

def decodificar_pixels(height, width, tree, bitstream):
    pixels = np.empty((height, width, 3), dtype=np.uint16)
    for i in range(height):
        for j in range(width):
            for channel in range(3):
                pixels[i, j, channel] = decodificar_valor(tree, bitstream)
    return pixels

def decompress_image(in_file_name):
    stream = InputBitStream(in_file_name)
    height, width = decodificar_cabecalho(stream)
    stream.flush()
    trimmed_tree = decodificar_arvore(stream)
    stream.flush()
    pixels = decodificar_pixels(height, width, trimmed_tree, stream)
    stream.close()
    return pixels