from PIL import Image
import numpy as np

# Função para realizar a convolução entre a imagem e o kernel
def convolucao(image, kernel):
    width, height = image.size
    kernel_width, kernel_height = kernel.shape
    padding = kernel_width // 2
    
    # Cria uma nova imagem vazia para armazenar o resultado
    result = Image.new((width, height))

    for x in range(padding, width - padding):
        for y in range(padding, height - padding):
            accumulator = 0
            for i in range(-padding, padding + 1):
                for j in range(-padding, padding + 1):
                    pixel_value = image.getpixel((x + i, y + j))
                    accumulator += pixel_value * kernel[i + padding, j + padding]
            result.putpixel((x, y), int(accumulator))

    return result

# Carrega a imagem com Pillow
image = Image.open('modificado.tif')  # Converte para escala de cinza

# Define um kernel de convolução (exemplo: filtro de média)
kernel = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1,1,1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) / 25

# Aplica a convolução manualmente
# result_image = convolucao(image, kernel)

# Exibe a imagem resultante
# result_image.show()
import numpy as np

# Crie um array NumPy com zeros de forma (linhas, colunas)
zeros_array = np.zeros((3, 4))

print(zeros_array)
