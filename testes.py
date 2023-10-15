from PIL import Image

# Crie uma imagem com 1 pixel
imagem = Image.new("RGB", (1, 1))

# Defina a cor desse único pixel (vermelho, verde, azul)
imagem.putpixel((0, 0), (40, 39, 112))  # Exemplo: pixel vermelho

# Salve a imagem com 1 pixel
imagem.save("imagem_com_1_pixel.jpg")