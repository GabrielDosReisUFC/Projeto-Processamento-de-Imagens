import numpy as np
from cmath import exp, pi
import matplotlib.pyplot as plt
from PIL import Image

#Transformada discreta ingênua de Fourier
'''def DFT2D(img, salvar):
    imagem = plt.imread(img)
    f = np.array(imagem)
    F = np.zeros(f.shape, dtype=np.complex64)
    n,m = f.shape[0:2]
    x = np.arange(n)
    # pra cada frequência u, v
    for u in np.arange(n):
        for v in np.arange(m):
            for y in np.arange(m):
                F[u,v] += np.sum(f[:,y] * np.exp( (-1j*2*np.pi) * (((u*x)/n)+((v*y)/m)) ))
    img_nova = F/np.sqrt(n*m)
    img_nova.save(salvar)'''

def DFT(img, salvar):
    img = Image.open(img)
    if img.mode == 'RGB':
        img = img.convert('L')  
    img_array = np.array(img)
    n, m = img_array.shape
    F = np.zeros((n, m), dtype=np.complex64)
    x = np.arange(n)

    for u in range(n):
        for v in range(m):
            for y in range(m):
                F[u, v] += np.sum(img_array[:, y] * np.exp((-1j * 2 * np.pi) * (((u * x) / n) + ((v * y) / m))))

    img_nova = np.real(F) / np.sqrt(n * m)
    magnitude_image = Image.fromarray(np.uint8(img_nova))
    magnitude_image.save(salvar)
    magnitude_image.close()

#Inversa
def IDFT2D(F):
    f = np.zeros(F.shape, dtype=np.int32)
    n,m = F.shape[0:2]
    u = np.arange(n)
    for x in np.arange(n):
        for y in np.arange(m):
            for v in np.arange(m):
                f[x,y] += np.real(np.sum(F[:,v] * np.exp( (1j*2*np.pi) * (((u*x)/n)+((v*y)/m)) )))
    np.real(f/np.sqrt(n*m))
    return

#Rápida - recursiva divisão e conquista
def FFT(img, salvar):
    img = Image.open(img)
    if img.mode == 'RGB':
        img = img.convert('L')
    img_array = np.array(img)
    fft_result = np.fft.fftshift(np.fft.fft2(img_array))
    magnitude = np.abs(fft_result)  
    magnitude_image = Image.fromarray(np.uint8(magnitude))
    magnitude_image.save(salvar)
    magnitude_image.close()
