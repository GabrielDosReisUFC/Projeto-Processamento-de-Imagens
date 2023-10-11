import numpy as np
import imageio
import matplotlib.pyplot as plt
import time
from cmath import exp, pi

def FFT(f):
    N = len(f)
    if N <= 1:
        return f
    
    # division
    even= FFT(f[0::2])
    odd = FFT(f[1::2])

    # store combination of results
    temp = np.zeros(N).astype(np.complex64)
    
    # only required to compute for half the frequencies 
    # since u+N/2 can be obtained from the symmetry property
    for u in range(N//2):
        temp[u] = even[u] + exp(-2j*pi*u/N) * odd[u] # conquer
        temp[u+N//2] = even[u] - exp(-2j*pi*u/N)*odd[u]  # conquer
                
    return temp