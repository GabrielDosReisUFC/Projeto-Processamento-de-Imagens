import cv2 
import numpy as np
from PIL import Image,ImageDraw

def chroma (img, imgfundo, gthreshold)

    width = img.shape[1]
    height = img.shape[0]
    dim = (width ,height)

    im_b,im_g,im_r = cv2.split(img



#Thresholder da imagem Green(G) e inversão da imagem com 'cv2.THRESH_BINARY_INV'
    ret,im_thresh1 = cv2.threshold(im_g,255-gthreshold,255,cv2.THRESH_BINARY_INV)

    Im_RGB = cv2.cvtColor(im_thresh1,cv2.COLOR_GRAY2BGR)

    im_noback = cv2.bitwise_and(Im_RGB, im)

#converto para RGB o resultado e mostro a imagem resultante.
    im_noback = cv2.cvtColor(im_noback,cv2.COLOR_BGR2RGB)


# Lendo Imagem que será o plano de fundo.

# Convertendo para RGB a imagem.
    z = cv2.cvtColor(imgfundo,cv2.COLOR_BGR2RGB)

# Plotando a imagem de backround e redimencionando a imagem de back.

    im_res = cv2.resize(z, dim, interpolation = cv2.INTER_AREA)

# Invete a imagem do thresholder
    im_iv = 255 - Im_RGB

    im_z_nofront = cv2.bitwise_and(im_res, im_iv)

# Soma da background com o frontend
    im_final = im_z_nofront + im_noback
    im_final.show()

