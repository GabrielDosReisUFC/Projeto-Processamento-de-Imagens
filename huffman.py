from PIL import Image
import numpy as np
from collections import Counter
import codificacao_preditiva

def to_binary_list_16(n):
    return [n] if (n <= 1) else to_binary_list_16(n >> 1) + [n & 1]

def from_binary_list_16(bits):
    result = 0
    for bit in bits:
        result = (result << 1) | bit
    return result

def pad_bits_16(bits, n):
    assert(n >= len(bits))
    return ([0] * (n - len(bits)) + bits)

def count_symbols(image):
    pixels = image.flatten()
    counts = Counter(pixels).items()
    return sorted(counts, key=lambda x: x[::-1])

def build_tree(counts):
    nodes = [entry[::-1] for entry in counts]
    while len(nodes) > 1:
        leastTwo = tuple(nodes[0:2])
        theRest = nodes[2:]
        combFreq = leastTwo[0][0] + leastTwo[1][0]
        nodes = theRest + [(combFreq, leastTwo)]
        nodes.sort(key=lambda x: x[0])  # Usando x[0] para ordenar pela frequência
    return nodes[0]

def trim_tree(tree):
    p = tree[1]
    if type(p) is tuple:
        return (trim_tree(p[0]), trim_tree(p[1]))
    return p

def assign_codes_impl(codes, node, pat):
    if type(node) == tuple:
        assign_codes_impl(codes, node[0], pat + [0])
        assign_codes_impl(codes, node[1], pat + [1])
    else:
        codes[node] = pat

def assign_codes(tree):
    codes = {}
    assign_codes_impl(codes, tree, [])
    return codes

class OutputBitStream(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'wb')
        self.bytes_written = 0
        self.buffer = []

    def write_bit(self, value):
        self.write_bits([value])

    def write_bits(self, values):
        self.buffer += values
        while len(self.buffer) >= 8:
            self._save_byte()

    def flush(self):
        if len(self.buffer) > 0:
            self.buffer += [0] * (8 - len(self.buffer))
            self._save_byte()
        assert(len(self.buffer) == 0)

    def _save_byte(self):
        bits = self.buffer[:8]
        self.buffer[:] = self.buffer[8:]

        byte_value = from_binary_list_16(bits)
        if 0 <= byte_value <= 255:
            self.file.write(bytes([byte_value]))
            self.bytes_written += 1
        else:
            raise ValueError(f"Invalid byte value: {byte_value}")

    def close(self):
        self.flush()
        self.file.close()

def encode_header(image, bitstream):
    height_bits = pad_bits_16(to_binary_list_16(image.shape[0]), 16)
    bitstream.write_bits(height_bits)
    width_bits = pad_bits_16(to_binary_list_16(image.shape[1]), 16)
    bitstream.write_bits(width_bits)

def encode_tree(tree, bitstream):
    if type(tree) == tuple:
        bitstream.write_bit(0)
        encode_tree(tree[0], bitstream)
        encode_tree(tree[1], bitstream)
    else:
        bitstream.write_bit(1)
        symbol_bits = pad_bits_16(to_binary_list_16(tree), 16)
        bitstream.write_bits(symbol_bits)

def encode_pixels(image, codes, bitstream):
    pixels = image.flatten()
    for value in pixels:
        bitstream.write_bits(codes[value])

def compressed_size(counts, codes):
    header_size = 2 * 16  # height and width as 16-bit values

    tree_size = len(counts) * (1 + 16)  # Leafs: 1 bit flag, 16-bit symbol each
    tree_size += len(counts) - 1  # Nodes: 1 bit flag each
    if tree_size % 8 > 0:  # Padding to next full byte
        tree_size += 8 - (tree_size % 8)

    pixels_size = sum([count * len(codes[symbol]) for symbol, count in counts])
    if pixels_size % 8 > 0:  # Padding to next full byte
        pixels_size += 8 - (pixels_size % 8)

    return (header_size + tree_size + pixels_size) / 8

def compress_array(array, out_file_name):
    size_raw = array.shape
    counts = count_symbols(array)
    tree = build_tree(counts)
    trimmed_tree = trim_tree(tree)
    codes = assign_codes(trimmed_tree)
    size_estimate = compressed_size(counts, codes)
    stream = OutputBitStream(out_file_name)
    encode_header(array, stream)
    stream.flush() 
    encode_tree(trimmed_tree, stream)
    stream.flush()
    encode_pixels(array, codes, stream)
    stream.close()

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
        self.buffer += pad_bits_16(to_binary_list_16(value), 8)
        self.bytes_read += 1

    def close(self):
        self.file.close()


def decode_header(bitstream):
    height = from_binary_list_16(bitstream.read_bits(16))
    width = from_binary_list_16(bitstream.read_bits(16))
    return (height, width)

def decode_tree(bitstream):
    flag = bitstream.read_bits(1)[0]
    if flag == 1:
        return np.uint16(from_binary_list_16(bitstream.read_bits(16)))
    left = decode_tree(bitstream)
    right = decode_tree(bitstream)
    return (left, right)

def decode_value(tree, bitstream):
    bit = bitstream.read_bits(1)[0]
    node = tree[bit]
    if type(node) == tuple:
        return decode_value(node, bitstream)
    return np.uint16(node)

def decode_pixels(height, width, tree, bitstream):
    pixels = np.empty((height, width, 3), dtype=np.uint16)
    for i in range(height):
        for j in range(width):
            for channel in range(3):
                pixels[i, j, channel] = decode_value(tree, bitstream)
    return pixels

def decompress_image(in_file_name):
    stream = InputBitStream(in_file_name)
    height, width = decode_header(stream)
    stream.flush()
    trimmed_tree = decode_tree(stream)
    stream.flush()
    pixels = decode_pixels(height, width, trimmed_tree, stream)
    stream.close()
    return pixels