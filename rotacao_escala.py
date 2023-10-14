import numpy as np 
import cv2
import math as m 
import sys

img = cv2.imread(sys.argv[1])
angle = sys.argv[2]

#get rotation matrix
def getRMat(cx, cy, angle, scale):
    a = scale*m.cos(angle*np.pi/180)
    b = scale*(m.sin(angle*np.pi/180))
    u = (1-a)*cx-b*cy
    v = b*cx+(1-a)*cy
    return np.array([[a,b,u], [-b,a,v]]) 

#determine shape of img
h, w = img.shape[:2]
#print h, w
#determine center of image
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

dst = warpAff2(img, mat, newWidth, newHeight)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

def warpAff(image, matrix, width, height):
    dst = np.zeros((width, height, 3), dtype=np.uint8)
    oldh, oldw = image.shape[:2]
    # Loop over the destination, not the source, to ensure that you cover
    # every destination pixel exactly 1 time, rather than 0-4 times.
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
                dst[u, v] = image[intx, inty]
    return dst


dst = warpAff(img, mat, (newWidth, newHeight))

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()