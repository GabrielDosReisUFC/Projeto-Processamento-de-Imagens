import numpy as np
import matplotlib.pyplot as plt
from cmath import exp, pi

def FFT(f):
    N = len(f)
    if N <= 1:
        return f
    even= FFT(f[0::2])
    odd = FFT(f[1::2])
    temp = np.zeros(N).astype(np.complex64)
    for u in range(N//2):
        temp[u] = even[u] + exp(-2j*pi*u/N) * odd[u] 
        temp[u+N//2] = even[u] - exp(-2j*pi*u/N)*odd[u]  
                
    return temp