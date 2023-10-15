from PIL import Image
import numpy as np 


def limearizar(image_path,valor,salvar):
    imagem = Image.open(image_path)
    if imagem.mode == "RGB" or imagem.mode == "HSV":
        imagem.close()
        limearizar_RGB(image_path,valor,salvar)
    else:
        imagem.close()
        limearizar_simples(image_path,valor,salvar)

def limearizar_RGB(image_path,valor,salvar):
    image = Image.open(image_path)
    imagem_array = np.array(image)
    canal_r =  imagem_array[:,:,0]
    canal_g =  imagem_array[:,:,1]
    canal_b =  imagem_array[:,:,2]

    canal_r[canal_r<valor] = 0
    canal_g[canal_g<valor] = 0
    canal_b[canal_b<valor] = 0

    imagem_modificada_array = np.stack((canal_r, canal_g, canal_b), axis=-1)

    # Crie uma imagem PIL a partir do array resultante
    imagem_modificada = Image.fromarray(imagem_modificada_array)
    image.close()
    # Salve a imagem modificada
    imagem_modificada.save(salvar)
    

def limearizar_simples(image_path,valor,salvar):
    img_aux = Image.open(image_path)
    # dados_imagem = np.array(image_path)
    for x in range(img_aux.height):
        for y in range(img_aux.width):
            # print(x,y)
            pixel = int(img_aux.getpixel((y, x)))
            # if round(dados_imagem[x,y]) < valor:
            if pixel <= valor:
                img_aux.putpixel((y, x), 0)
            else:
                img_aux.putpixel((y, x), 255)
    
    img_aux.save(salvar)
    img_aux.close()

limearizar_RGB("cubo.tif",254,"modificado.tif")