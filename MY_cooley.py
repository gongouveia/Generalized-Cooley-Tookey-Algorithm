
from scipy.fft import fft
import numpy as np

x = np.array([1,1,1,5,1,1,5,1,1])



def DFT(x):
    """
    Function to calculate the 
    discrete Fourier Transform 
    of a 1D real-valued signal x
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    
    X = np.dot(e, x)
    
    return X

def twiddle_matrix(a,b):
    N = a*b
    aux=[]
    for j in range(b):
        for i in range(a):
            k = i*j
            aux.append(np.exp(-1j*2*np.pi*k/N))
    return np.array(aux)



def dft_of_rows(x,a,b):
    print('\nMatrix')
    step1 = x.reshape(b,a).T
    print(step1)

    print('\nDFT of each Row')
    step2 = []
    for i in step1:
        step2.append(fft(i,a))
        #step2.append(DFT(i))
    step2 = np.array(step2).reshape(b,a)
    print(step2)
    return step2

def calculate_multiply_twidles(x,a,b):
    print('\ntwiddles')
    print(twiddle_matrix(a,b).reshape(b,a))


    print('\nMultiplication twiddle and After rowDFT')
    after_mult = twiddle_matrix(a,b).reshape(b,a)*x
    print(after_mult)
    return after_mult


def DFT_of_collumns(x,a,b):
    print('\n Transpose')
    trans = x.T

    print(trans)
    print('\nDFT of each Collumn')
    step3 = []
    for i in trans:
        #step3.append(fft(i,b))
        step3.append(DFT(i))
    step3 = np.array(step3).reshape(b,a)
    print(step3.T)
    return step3

a = 3
b = 3
first_step = dft_of_rows(x,a,b)
cmatrix_multiplied = calculate_multiply_twidles(first_step,a,b)
final_matrix = DFT_of_collumns(cmatrix_multiplied,a,b)


print('\nDFT true')
print(fft(x,9))

