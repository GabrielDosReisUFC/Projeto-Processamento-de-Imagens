from PIL import Image
import retornarPath
def limearizar(image_path,valor):
    # Abra a imagem .tif
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
    
    return retornarPath.path(image_path,img_aux)
