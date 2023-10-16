from PIL import Image
import numpy as np

def chromakey(img_path, background_path, gthreshold, salvar):
    img = Image.open(img_path)
    background = Image.open(background_path)

    # Certifique-se de que as imagens de entrada tenham as mesmas dimensões
    if img.size != background.size:
        # Se as dimensões forem diferentes, redimensione a imagem de fundo
        background = background.resize(img.size, Image.ANTIALIAS)

    img_array = np.array(img)
    im_g = img_array[:, :, 1]

    im_thresh = (im_g > (255 - gthreshold)).astype(np.uint8) * 255
    im_thresh = np.stack((im_thresh, im_thresh, im_thresh), axis=-1)

    im_noback = im_thresh * img_array

    background_array = np.array(background)
    im_iv = 255 - im_thresh
    im_z_nofront = im_iv * background_array

    im_final = im_z_nofront + im_noback

    # Converte a imagem resultante de volta para o formato PIL (Image)
    im_final_pil = Image.fromarray(im_final.astype(np.uint8))

    # Salva a imagem resultante
    im_final_pil.save(salvar)


