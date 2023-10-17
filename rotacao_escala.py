import numpy as np 
import math as m 
from PIL import Image


#matriz de rotação

def MatR(cx, cy, angle, scale):
    a = scale*m.cos(angle*np.pi/180)
    b = scale*(m.sin(angle*np.pi/180))
    u = (1-a)*cx-b*cy
    v = b*cx+(1-a)*cy
    return np.array([[a,b,u], [-b,a,v]]) 

def mapeamento(img, matrix, width, height):
        mapa = np.zeros((height, width, 3), dtype=np.uint8)
        w = img.width
        h = img.height
        for u in range(width):
            for v in range(height):
                x = u*matrix[0,0]+v*matrix[0,1]+matrix[0,2]
                y = u*matrix[1,0]+v*matrix[1,1]+matrix[1,2]
                intx, inty = int(x), int(y)
                if 0 < intx < w and 0 < inty < h:
                    mapa [v,u] = img.getpixel((intx, inty))
        return mapa

def rotacao(img,valor,salvar):
    angulo = valor
    img = Image.open(img)
    img = img.convert("RGB")
    w = img.width
    h = img.height
    cx, cy = (w / 2, h / 2)
    mat = MatR(cx, cy, int(angulo), 1)
    cos = np.abs(mat[0,0])
    sin  = np.abs(mat[0,1])
    nova_w = int((h * sin) + (w * cos))
    nova_h = int((h * cos) + (w * sin))
    mat[0,2] += cx - (nova_w / 2)
    mat[1,2] += cy - (nova_h / 2)
    img_nova = mapeamento(img, mat, nova_w, nova_h)
    img = Image.fromarray(img_nova)
    img.save(salvar)
    img.close()

#interpolaçao pelo vizinho mais próximo
def interpolacao_nn(img, escala, salvar):
    img = Image.open(img)
    w, h = img.size
    nova_h = int(h * escala)
    nova_w = int(w * escala)
    img_nova = Image.new("RGB", (nova_w, nova_h))
    for i in range(nova_h):
        for j in range(nova_w):
            x = int(i / escala)
            y = int(j / escala)
            img_nova.putpixel((j, i), img.getpixel((y, x)))
    img_nova.save(salvar)
    img_nova.close()
    img.close()

# Função para realizar a interpolação linear
def interpolacao_lin(img, escala, salvar):
    img = Image.open(img)
    w, h = img.size
    nova_h = int(h * escala)
    nova_w = int(w * escala)
    img_nova = Image.new("RGB", (nova_w, nova_h))
    for i in range(nova_h):
        for j in range(nova_w):
            x = i / escala
            y = j / escala
            x0, y0 = int(x), int(y)
            x1, y1 = x0 + 1, y0 + 1
            if x1 >= h:
                x1 = x0
            if y1 >= w:
                y1 = y0
            dx, dy = x - x0, y - y0
            pixel = (
                int((1 - dx) * (1 - dy) * img.getpixel((y0, x0))[0] + dx * (1 - dy) * img.getpixel((y0, x1))[0] + (1 - dx) * dy * img.getpixel((y1, x0))[0] + dx * dy * img.getpixel((y1, x1))[0]),
                int((1 - dx) * (1 - dy) * img.getpixel((y0, x0))[1] + dx * (1 - dy) * img.getpixel((y0, x1))[1] + (1 - dx) * dy * img.getpixel((y1, x0))[1] + dx * dy * img.getpixel((y1, x1))[1]),
                int((1 - dx) * (1 - dy) * img.getpixel((y0, x0))[2] + dx * (1 - dy) * img.getpixel((y0, x1))[2] + (1 - dx) * dy * img.getpixel((y1, x0))[2] + dx * dy * img.getpixel((y1, x1))[2])
            )
            img_nova.putpixel((j, i), pixel)
    img_nova.save(salvar)
    img_nova.close()
    img.close()
