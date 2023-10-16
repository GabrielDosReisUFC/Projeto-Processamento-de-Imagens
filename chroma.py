import cv2 
import numpy as np
from PIL import Image,ImageDraw

def chromakey(img, imgfundo, gthreshold, salvar):

    img=Image.open(img)
    dim = (img.width ,img.height)

    im_b,im_g,im_r = cv2.split(img)

    ret,im_thresh1 = cv2.threshold(im_g,255-gthreshold,255,cv2.THRESH_BINARY_INV)

    Im_RGB = cv2.cvtColor(im_thresh1,cv2.COLOR_GRAY2BGR)

    im_noback = cv2.bitwise_and(Im_RGB, img)

    im_noback = cv2.cvtColor(im_noback,cv2.COLOR_BGR2RGB)

    z = cv2.cvtColor(imgfundo,cv2.COLOR_BGR2RGB)

    im_res = cv2.resize(z, dim, interpolation = cv2.INTER_AREA)

    im_iv = 255 - Im_RGB

    im_z_nofront = cv2.bitwise_and(im_res, im_iv)

    im_final = im_z_nofront + im_noback

    im_final.save(salvar)