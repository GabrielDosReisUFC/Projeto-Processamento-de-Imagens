import colorsys
import math

def RGB_HSV(R,G,B):
    H = 0 ; S = 0 ; V = 0
    R = R/ 255; G = G/ 255; B = B/ 255; 
    C_max = max(R,G,B)
    C_min = min(R,G,B)
    delta = C_max - C_min
    
    if delta == 0:
        pass
    elif C_max == R:
        H = 60 * (((G-B)/delta)%6)
    elif C_max == G:
        H = 60 * ((B-R)/delta+2)
    elif C_max == B:
        H = 60 * ((R-G)/delta+4)

    if C_max == 0:
        S = 0
    else:
        S = delta/C_max * 100

    V = C_max * 100

    return math.floor(H),math.floor(S),math.floor(V)

def HSV_RGB(H,S,V):
    S = S/100
    V = V/100
    R = 0; G = 0; B = 0
    C = V * S
    X = C * (1-abs((H/60)%2-1))
    m = V-C

    if H < 60:
        R = C
        G = X
        B = 0
    elif H < 120:
        R = X
        G = C
        B = 0
    elif H < 180:
        R = 0
        G = C
        B = X
    elif H < 240:
        R = 0
        G = X
        B = C
    elif H < 300:
        R = X
        G = 0
        B = C
    else:
        R = C
        G = 0
        B = X

    R = (R+m)*255
    G = (G+m)*255
    B = (B+m)*255

    print(R,G,B)
    return math.floor(R),math.floor(G),math.floor(B)

def escala_cinza(r,g,b):
    cinza = (r+g+b)//3
    return cinza

def escala_cinza_ponderada(r,g,b,peso1,peso2,peso3):
    cinza = (peso1*r,peso2*g,peso3*b)
    return cinza

def negativo(r,g,b):
    neg_r = 255 - r
    neg_g = 255 - g
    neg_b = 255 - b
    return neg_r,neg_g,neg_b

def serpia(r,g,b):
    serpia_r = (0.393 * r + 0.769 * g + 0.189 * b)
    serpia_g = (0.349 * r + 0.686 * g + 0.168 * b)
    serpia_b = (0.272 * r + 0.534 * g + 0.131 * b)

    return serpia_r,serpia_g,serpia_b
HSV_RGB(302,63,99)