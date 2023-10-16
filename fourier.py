import numpy as np
from cmath import exp, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#Transformada discreta ingênua de Fourier
def DFT2D(img, salvar):
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

#Rápida - recursiva divisão e conquista
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

def plot_spectrum(F):
    magnitude_spectrum = np.abs(F)
    plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
    plt.title('Espectro')
    plt.colorbar()

def edit_spectrum_with_brush(F, canvas):
    def edit(event):
        x, y = int(event.xdata), int(event.ydata)
        radius = 5  # Tamanho do pincel
        mask = np.zeros(F.shape)
        for i in range(x - radius, x + radius + 1):
            for j in range(y - radius, y + radius + 1):
                if 0 <= i < F.shape[1] and 0 <= j < F.shape[0]:
                    mask[j, i] = 1  # Define os pontos dentro do raio do pincel como 1
        F *= (1 - mask)  # Inverte os pontos clicados de preto para branco

        canvas.figure.clf()
        plot_spectrum(F)
        canvas.draw()

    return edit

def apply_user_modifications(F):
    modified_F = F  
    filtered_image = IDFT2D(modified_F)  
    return filtered_image