from PIL import Image,ImageTk

# Função para ocultar uma mensagem em uma imagem
def hide_message(image_path, message, output_path):
    # Abra a imagem .tif
    img = Image.open(image_path)
    
    # Converta a mensagem em uma sequência de bytes
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Verifique se a mensagem cabe na imagem
    print(len(binary_message),img.width * img.height)
    if len(binary_message) > img.width * img.height:
        print(1)
        raise ValueError("A mensagem é muito longa para ser ocultada na imagem.")

    data_index = 0

    # Percorra cada pixel da imagem
    for x in range(img.width):
        for y in range(img.height):
            pixel = int(img.getpixel((x, y)))

            # Modifique o último bit de cada canal RGB para ocultar a mensagem
            
            if data_index < len(binary_message):
                pixel = pixel & ~1 | int(binary_message[data_index])
                data_index += 1

            # Atualize o pixel na imagem
            img.putpixel((x, y), pixel)
    
    # Salve a imagem resultante
    img.save(output_path)

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
    return text

# Exemplo de uso
if __name__ == "__main__":
    # Oculte uma mensagem em uma imagem .tif
    hide_message("modificado.tif", "Mensagem secreta", "imagem_oculta.tif")

    # Extraia a mensagem da imagem oculta .tif
    extracted_message = extract_and_display_message("imagem_oculta.tif")
    