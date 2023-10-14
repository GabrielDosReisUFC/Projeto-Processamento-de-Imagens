import cv2
import colorsys
import numpy as np

def rgb_to_hsv(rgb_image):
    h, s, v = np.zeros_like(rgb_image), np.zeros_like(rgb_image), np.zeros_like(rgb_image)
    for i in range(rgb_image.shape[0]):
        for j in range(rgb_image.shape[1]):
            r, g, b = rgb_image[i, j]
            h[i, j], s[i, j], v[i, j] = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            h[i, j] *= 360
            s[i, j] *= 100
            v[i, j] *= 100
    return np.uint8(h), np.uint8(s), np.uint8(v)

# Carregue a imagem em formato BGR (OpenCV usa BGR, não RGB)
bgr_image = cv2.imread("mulher.tif")

# Converta de BGR para RGB
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

# Converta de RGB para HSV manualmente
h, s, v = rgb_to_hsv(rgb_image)

# Combine os canais H, S e V em uma imagem HSV
hsv_image = cv2.merge([h, s, v])

# Salve a imagem convertida em HSV
cv2.imwrite("imagem_hsv_manual.png", hsv_image)

# Lembre-se de substituir "exemplo.png" pelo caminho da sua imagem original.
