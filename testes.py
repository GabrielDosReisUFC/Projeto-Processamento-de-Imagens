from PIL import Image

# Carregue a imagem original
imagem_original = Image.open('fundo.jpg')

# Define a cor de fundo que você deseja substituir (verde no formato RGB)
cor_de_fundo_min = 150
cor_de_fundo_max = 220
# Carregue a imagem de substituição
imagem_substituicao = Image.open('praia.jpg')
imagem_substituicao = imagem_substituicao.resize((imagem_original.width, imagem_original.height))
# Crie uma máscara para isolar a cor de fundo
mascara = Image.new('L', imagem_original.size)
for x in range(imagem_original.width):
    for y in range(imagem_original.height):
        pixel = imagem_original.getpixel((x, y))
        r,g,b = pixel[:3] 
        # if cor_de_fundo_min < pixel[:3] :
        if cor_de_fundo_min< g and g < cor_de_fundo_max :
            mascara.putpixel((x, y), 255)
        else:
            mascara.putpixel((x, y), 0)

# Combinar a imagem original e a imagem de substituição usando a máscara
imagem_final = Image.composite(imagem_substituicao, imagem_original, mascara)

# Salvar a imagem resultante
imagem_final.show()
