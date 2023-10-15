import numpy as np
from cmath import exp, pi

#Transformada discreta ingênua de Fourier
def DFT2D(f):
    F = np.zeros(f.shape, dtype=np.complex64)
    n,m = f.shape[0:2]
    x = np.arange(n)
    # pra cada frequência u, v
    for u in np.arange(n):
        for v in np.arange(m):
            for y in np.arange(m):
                F[u,v] += np.sum(f[:,y] * np.exp( (-1j*2*np.pi) * (((u*x)/n)+((v*y)/m)) ))
    return F/np.sqrt(n*m)

#Inversa
def IDFT2D(F):
    f = np.zeros(F.shape, dtype=np.int32)
    n,m = F.shape[0:2]
    u = np.arange(n)
    for x in np.arange(n):
        for y in np.arange(m):
            for v in np.arange(m):
                f[x,y] += np.real(np.sum(F[:,v] * np.exp( (1j*2*np.pi) * (((u*x)/n)+((v*y)/m)) )))
    return np.real(f/np.sqrt(n*m))

#Rápida
def FFT(f):
    N = len(f)
    if N <= 1:
        return f
    par = FFT(f[0::2])
    impar = FFT(f[1::2])
    aux = np.zeros(N).astype(np.complex64)
    for u in range(N//2):
        aux[u] = par[u] + exp(-2j*pi*u/N) * impar[u] 
        aux[u+N//2] = par[u] - exp(-2j*pi*u/N)*impar[u]  
                
    return aux

def fftshift(x, axes=None):
    x = asarray(x)
    if axes is None:
        axes = tuple(range(x.ndim))
        shift = [dim // 2 for dim in x.shape]
    elif isinstance(axes, integer_types):
        shift = x.shape[axes] // 2
    else:
        shift = [x.shape[ax] // 2 for ax in axes]

    return roll(x, shift, axes)


def ffiltro(tamanho,img):
    img_s = img[:tamanho, :tamanho]
    Fs = DFT2D(img_s)
    imshow(np.log(1 + fftshift(np.abs(Fs))))