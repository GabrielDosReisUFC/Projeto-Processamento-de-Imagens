import numpy as np
import pywt
from PIL import Image

def compress_image(image_path, output_path, num_levels=2):
    # Load the image
    original_image = Image.open(image_path)

    # Convert the image to a numpy array
    img_array = np.array(original_image)

    # Split the image into its RGB channels
    red_channel, green_channel, blue_channel = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

    # Apply DWT to each channel
    compressed_red = compress_channel(red_channel, num_levels)
    compressed_green = compress_channel(green_channel, num_levels)
    compressed_blue = compress_channel(blue_channel, num_levels)

    # Combine the compressed channels back into an image
    compressed_image_array = np.stack([compressed_red, compressed_green, compressed_blue], axis=-1)

    # Convert the array back to a Pillow image
    compressed_image = Image.fromarray(np.uint8(compressed_image_array))

    # Save the compressed image
    compressed_image.save(output_path)

def compress_channel(channel, num_levels):
    # Apply 2D Discrete Wavelet Transform
    coeffs = pywt.wavedec2(channel, 'haar', level=num_levels)

    # Set some threshold for coefficients (experiment with this value)
    threshold = 30.0

    # Threshold and quantize coefficients
    quantized_coeffs = [pywt.threshold(c, threshold, mode='soft') if isinstance(c, np.ndarray) else c for c in coeffs]

    # Apply 2D Inverse Wavelet Transform
    compressed_channel = pywt.waverec2(quantized_coeffs, 'haar')

    # Ensure the values are within the valid range (0-255)
    compressed_channel = np.clip(compressed_channel, 0, 255)

    # Round to integers
    compressed_channel = np.round(compressed_channel)

    return compressed_channel.astype(np.uint8)

input_image_path = "testes/cubo.tif"  # Replace with the path to your BMP image
output_image_path = "compressed_image.bmp"  # Change the output filename as needed

compress_image(input_image_path, output_image_path)
