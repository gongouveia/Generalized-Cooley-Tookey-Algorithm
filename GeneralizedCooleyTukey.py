import numpy as np
from scipy.fft import fft
import math

def twiddle_factors(a,b):
    N = a*b
    k = np.arange(N)
    e = np.exp(-2j * np.pi * k  / N)
    print('Twiddles calculated:')
    print(e)
    return e



class FFTOperations:
    def test(a, b):
        # matrix is n1 x n2, a is n1, b is n2
        np.random.seed(10)
        #generate random values to fill the matrix
        temp = []
        for i in range(a):
            row = []
            for k in range(b):
                row.append(np.random.uniform(-1.0, 1.0) + np.random.uniform(-1.0, 1.0)*1j)
            temp.append(row)
        #temp = [[1+0j,0+0j],[1+0j,0+0j]]
        cooley_tukey = np.array(temp)
        
        print('\nOriginal: \n' + str(cooley_tukey))
        
        #1st FFT
        for i in range(a):
            cooley_tukey[i] = fft(cooley_tukey[i],b)
        print('\n1st FFT: \n' + str(cooley_tukey))
        
        
        #Transpose the matrix
        cooley_tukey = cooley_tukey.transpose()
        print('\nTransposed: \n' + str(cooley_tukey))
        
        #2nd FFT
        for i in range(b):
            cooley_tukey[i] = fft(cooley_tukey[i],a)
        print('\n2nd FFT: \n' + str(cooley_tukey))
        #Reshape matrix for easier readability
        cooley_tukey = cooley_tukey.reshape([1,a*b])
        
        #Perform one large fft on entire dataset to comapre with Cooley-Tukey approach
        scipy_fft = np.array(temp)
        scipy_fft = scipy_fft.reshape([1,a*b])
        scipy_fft = fft(scipy_fft[0], a*b)
        print('\nCooley-Tukey: \n' + str(cooley_tukey[0]))
        print('\nScipy Package: \n' + str(scipy_fft))
        
b = FFTOperations
b.test(2,6)



twiddle_factors(2,6)