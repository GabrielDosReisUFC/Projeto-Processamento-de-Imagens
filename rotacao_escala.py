import numpy as np 
import cv2
import math as m 
import sys

def getRMat(cx, cy, angle, scale):
    a = scale*m.cos(angle*np.pi/180)
    b = scale*(m.sin(angle*np.pi/180))
    u = (1-a)*cx-b*cy
    v = b*cx+(1-a)*cy
    return np.array([[a,b,u], [-b,a,v]]) 


h, w = img.shape[:2]


cx, cy = (w / 2, h / 2)

mat = getRMat(cx, cy, int(angle), 1)
cos = np.abs(mat[0,0])
sin  = np.abs(mat[0,1])
newWidth = int((h * sin) + (w * cos))
newHeight = int((h * cos) + (w * sin))
mat[0,2] += cx - (newWidth / 2)
mat[1,2] += cy - (newHeight / 2)

def warpAff2(image, matrix, width, height):
        dst = np.zeros((height, width, 3), dtype=np.uint8)
        oldh, oldw = image.shape[:2]
        for u in range(width):
            for v in range(height):
                x = u*matrix[0,0]+v*matrix[0,1]+matrix[0,2]
                y = u*matrix[1,0]+v*matrix[1,1]+matrix[1,2]
                intx, inty = int(x), int(y)
                if 0 < intx < oldw and 0 < inty < oldh:
                    pix = image[inty, intx]
                    dst[v, u] = pix
        return dst

def rotacao(img,value,save):
    angle = value
    img = Image.open(img)
    def getRMat(cx, cy, angle, scale):
        a = scale*m.cos(angle*np.pi/180)
        b = scale*(m.sin(angle*np.pi/180))
        u = (1-a)*cx-b*cy
        v = b*cx+(1-a)*cy
        return np.array([[a,b,u], [-b,a,v]]) 
    h, w = img.shape[:2]
    cx, cy = (w / 2, h / 2)
    mat = getRMat(cx, cy, int(angle), 1)
    cos = np.abs(mat[0,0])
    sin  = np.abs(mat[0,1])
    newWidth = int((h * sin) + (w * cos))
    newHeight = int((h * cos) + (w * sin))
    mat[0,2] += cx - (newWidth / 2)
    mat[1,2] += cy - (newHeight / 2)
    img_nova = warpAff2(img, mat, newWidth, newHeight)
    img_nova.save(salvar)


def escala(image, matrix, width, height):
    image = Image.open(img)
    img_nova = np.zeros((width, height, 3), dtype=np.uint8)
    oldh, oldw = image.shape[:2]
    for u in range(width):
        for v in range(height):
            x = u*matrix[0,0]+v*matrix[0,1]+matrix[0,2]
            y = u*matrix[1,0]+v*matrix[1,1]+matrix[1,2]
            intx, inty = int(x), int(y)
            # We could interpolate here by using something like this linear
            # interpolation matrix, but let's keep it simple and not do that.
            # fracx, fracy = x%1, y%1
            # interp = np.array([[fracx*fracy, (1-fracx)*fracy],
            #                    [fracx*(1-fracy), (1-fracx)*(1-fracy)]])
            if 0 < x < oldw and 0 < y < oldh:
                img_nova[u, v] = image[intx, inty]
    img_nova.save(salvar)


def nearest_neighbor_interpolation(image, scale_factor):
    height, width = image.shape[:2]
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)
    new_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for i in range(new_height):
        for j in range(new_width):
            x = int(i / scale_factor)
            y = int(j / scale_factor)
            new_image[i, j] = image[x, y]

    return new_image

# Função para realizar a interpolação linear
def linear_interpolation(image, scale_factor):
    height, width = image.shape[:2]
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)
    new_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for i in range(new_height):
        for j in range(new_width):
            x = i / scale_factor
            y = j / scale_factor
            x0, y0 = int(x), int(y)
            x1, y1 = x0 + 1, y0 + 1
            if x1 >= height:
                x1 = x0
            if y1 >= width:
                y1 = y0
            dx, dy = x - x0, y - y0

            for channel in range(image.shape[2]):
                new_image[i, j, channel] = (1 - dx) * (1 - dy) * image[x0, y0, channel] + dx * (1 - dy) * image[x1, y0, channel] + (1 - dx) * dy * image[x0, y1, channel] + dx * dy * image[x1, y1, channel]

    return new_image