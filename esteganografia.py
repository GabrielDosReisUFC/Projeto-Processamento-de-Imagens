from PIL import Image

# Função para ocultar uma mensagem em uma imagem
def hide_message(image_path,message):
    path_temp = "modificado_escondido.tif"
    # Abra a imagem .tif
    img_aux = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Verifique se a mensagem cabe na imagem
    if len(binary_message) > img_aux.width * img_aux.height:
        raise ValueError("A mensagem é muito longa para ser ocultada na imagem.")

    data_index = 0

    # Percorra cada pixel da imagem
    for x in range(img_aux.width):
        for y in range(img_aux.height):
            pixel = int(img_aux.getpixel((x, y)))

            # Modifique o último bit de cada canal RGB para ocultar a mensagem
            
            if data_index < len(binary_message):
                pixel = pixel & ~1 | int(binary_message[data_index])
                data_index += 1

            # Atualize o pixel na imagem
            img_aux.putpixel((x, y), pixel)
    
    # Salve a imagem resultante
    img_aux.save(path_temp)
    img_aux.close()
    img = Image.open(path_temp)
    img.save(image_path)
    img.close()

# Função para extrair uma mensagem de uma imagem oculta
def extract_and_display_message(image_path):
    # Abra a imagem
    img = Image.open(image_path)

    binary_message = ""

    # Percorra cada pixel da imagem
    for x in range(img.width):
        for y in range(img.height):
            pixel = int(img.getpixel((x, y)))
                       
            binary_message += str(pixel & 1)
            

    # Converta a sequência de bits de volta para a mensagem original
    message = "".join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    text = ""
    for i in message:
        if i.isprintable():
            text += i
    img.close()
    return text
    