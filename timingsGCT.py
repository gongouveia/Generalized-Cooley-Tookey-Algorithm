
from scipy.fft import fft
from CTgeneralUTIL import DFT, twiddle_matrix, primefactors
import numpy as np
import matplotlib.pyplot as plt
import time
from numba import njit
import pandas as pd
def dft_of_rows(x,a,b):                            #rows DFT//FFT
    step1 = x.reshape(a,b).T
    #step2 = [fft(i,a) for i in step1]
    step2 = [DFT(i) for i in step1]

    return np.array(step2).reshape(b,a)

def twiddle_factors(a,b):                          #calcula a matriz de twiddle factors
    return twiddle_matrix(a,b).reshape(b,a)

def calculate_multiply_twidles(x,a,b, twiddle):
    return twiddle*x

def DFT_of_collumns(x,a,b):
    trans = x.T
    #step3 = [fft(i,b) for i in trans]
    step3 = [DFT(i) for i in trans]

    return np.array(np.array(step3))

def calculate_sci_fft(x,a,b):                      #FFT with scipy library
    return fft(x,a*b)

def calculate_np_fft(x,a,b):                     #FFT with scinumpypy library
    #return fft(x,a*b)
    return np.fft.fft(x,a*b)

def calculateCTG(x,a,b,twiddle):
    first_step = dft_of_rows(x,a,b)
    cmatrix_multiplied = calculate_multiply_twidles(first_step,a,b,twiddle)
    final_matrix = DFT_of_collumns(cmatrix_multiplied,a,b)
########################################################

#n = int(input("Enter the number for calculating the prime factors :\n"))
#primefactors(n)
xx = []
scipy_arr = []
dft_arr   = []
gtc_arr    = []
npy_arr = []
N_arr = []
for i in range(12):
    a = 5
    b = 2**i
    twiddle = twiddle_factors(a,b)

    xx.append(a*b)
    x = np.random.randint(1, size=(a*b))

    st = time.time()
    gtc = calculateCTG(x,a,b,twiddle)
    se = time.time()
    gtc_time = se-st
    print(se-st)

                        
    st = time.time()
    scipy_fft = calculate_sci_fft(x,a,b)
    se = time.time()
    scipy_time = se-st
    print(se-st)


    st = time.time()
    npfft = calculate_np_fft(x,a,b)
    se = time.time()
    npy_time = se-st
    print(se-st)  

    st = time.time()
    dftt_fft = DFT(x)
    se = time.time()
    dft_time = se-st
    print(se-st)


    scipy_arr.append(scipy_time)
    dft_arr.append(dft_time)
    gtc_arr.append(gtc_time)
    npy_arr.append(npy_time)
    N_arr.append(a*b)


df = pd.DataFrame()
df['Length'] = N_arr
df['Cooley Genrlzd'] = gtc_arr
df['numpy']  = npy_arr
df['scipy'] = scipy_arr 
df['DFT'] = dft_arr

print(df)

plt.plot(xx,npy_arr, label = 'numpy')
plt.plot(xx,gtc_arr, label = 'cooley')
plt.plot(xx,scipy_arr, label = 'scipy')
plt.plot(xx,dft_arr, label= 'DFT')
plt.legend()
plt.show()




#usar uma matriz?
#como adquirir valores em paralelo 
#como enviar os dados