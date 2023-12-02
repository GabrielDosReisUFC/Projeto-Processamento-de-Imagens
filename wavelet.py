import numpy as np
from PIL import Image

def haar_wavelet_transform(matrix):
    size = len(matrix)
    result = np.zeros_like(matrix)

    for i in range(size // 2):
        result[i, :] = (matrix[2 * i, :] + matrix[2 * i + 1, :]) / np.sqrt(2)
        result[i + size // 2, :] = (matrix[2 * i, :] - matrix[2 * i + 1, :]) / np.sqrt(2)

    return result

def inverse_haar_wavelet_transform(matrix):

    size = len(matrix)
    result = np.zeros_like(matrix)

    for i in range(size // 2):
        result[2 * i, :] = (matrix[i, :] + matrix[i + size // 2, :]) / np.sqrt(2)
        result[2 * i + 1, :] = (matrix[i, :] - matrix[i + size // 2, :]) / np.sqrt(2)

    return result

<<<<<<< HEAD
def wavelet_compress(image_path, output_path, wavelet_transform, inverse_wavelet_transform, level):

=======
# def wavelet_compress(image_path, output_path, wavelet_transform, inverse_wavelet_transform, level=1):
def compress(image_path, wavelet_transform=haar_wavelet_transform, inverse_wavelet_transform=inverse_haar_wavelet_transform, level=1):
>>>>>>> 8d88b07d43b0630b78d75f512609ed5d6a8cce8e
    img = Image.open(image_path)
    img_array = np.array(img)
    red_channel, green_channel, blue_channel = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
    compressed_red = haar_wavelet_transform(red_channel, level)
    compressed_green = haar_wavelet_transform(green_channel, level)
    compressed_blue = haar_wavelet_transform(blue_channel, level)
    compressed_image_array = np.stack([compressed_red, compressed_green, compressed_blue], axis=-1)

    # Convert the array back to a Pillow image
    compressed_image = Image.fromarray(np.uint8(compressed_image_array))
    compressed_image.save(output_path)


<<<<<<< HEAD
input_image_path = 'testes\cubo.tif'
output_compressed_image_path = 'output_compressed_image.bmp'
=======
    for i in range(img_array.shape[0]):
        img_array[i, :] = wavelet_transform(img_array[i, :])


    for i in range(img_array.shape[1]):
        img_array[:, i] = wavelet_transform(img_array[:, i])


    for _ in range(level):
        img_array[:2 ** (level - 1), :2 ** (level - 1)] = 0


    for i in range(img_array.shape[0]):
        img_array[i, :] = inverse_wavelet_transform(img_array[i, :])


    for i in range(img_array.shape[1]):
        img_array[:, i] = inverse_wavelet_transform(img_array[:, i])


    img_array = np.clip(img_array, 0, 255).astype(np.uint8)

    compressed_img = Image.fromarray(img_array)
    return compressed_img
    # compressed_img.save(output_path)

if __name__ == '__main__': 
    input_image_path = 'benchmark.bmp'
    output_compressed_image_path = 'output_compressed_image.bmp'

    compression_level = 5
>>>>>>> 8d88b07d43b0630b78d75f512609ed5d6a8cce8e

    # wavelet_compress(input_image_path, output_compressed_image_path, haar_wavelet_transform, inverse_haar_wavelet_transform, compression_level)
