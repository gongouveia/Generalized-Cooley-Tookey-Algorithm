from scipy.fft import fft
from CTgeneralUTIL import DFT, twiddle_matrix, primefactors
import numpy as np
import matplotlib.pyplot as plt
import time

from cmath import pi
import sys
import os
from time import time
import numpy as np
import matplotlib.pyplot as plt
import math
from math import *
import pandas as pd
import scipy
from scipy.signal import correlate
from handling import Handling
import csv
import pandas as pd
import random
from numpy import matrix as mat
#from ajuste_gaussiano import GaussAdj
#import polinom_approx as pa

# current=os.path.dirname(os.path.realpath(__file__))

# #before running this code, always be sure the file edit.csv is deleted 

# Data=Handling("/08_23_2022_13_58_arranquep.csv")
# Data.remove_empty_row("/edit.csv")
# data =Data.dataframe
# x = np.array(pd.DataFrame(data)['Real'])





def dft_of_rows(x,a,b):                                  #faz uma matriz com os valores formatados na ordem inicial e faz a DFT de cada linha
    step1 = x.reshape(a,b).T
    #step2 = [fft(i,a) for i in step1]
    step2 = [DFT(i) for i in step1]
    step2 = np.array(step2).reshape(b,a)
    print(f"DFT or rows: {step2}\n\n")
    return step2


def calculate_multiply_twidles(x,a,b):                  #caclula os twiddles factors e tarsnforma a matrix para um formato necesrio par ao proximo passo
    after_mult = twiddle_matrix(a,b).reshape(b,a)*x
    print(f"Multiply Twiddles:\n {after_mult}\n\n")
    return after_mult


def DFT_of_collumns(x,a,b):                     #calcula a DFT de cada coluna  e tem como output a matrix no formato final
    trans = x.T
    #step3 = [fft(i,b) for i in trans]
    step3 = [DFT(i) for i in trans]
    step3 = np.array(np.array(step3))
    print(f"DFT Collumns:\n {step3}\n\n")
    return step3


def calculateCTG(x,a,b):         #main function to calcuate our method clling above methods
    first_step = dft_of_rows(x,a,b)
    cmatrix_multiplied = calculate_multiply_twidles(first_step,a,b)
    final_matrix = DFT_of_collumns(cmatrix_multiplied,a,b)
    print(f"Final Matrix:\n {final_matrix}\n\n")
    return final_matrix


def calculate_sci_fft(x,a,b):     #calcula a FFt com a biblioteca Scipy
    print(f"calclated fft with scipy \n{fft(x,a*b)}")
    return fft(x,a*b)

########################################################

#n = int(input("Enter the number for calculating the prime factors :\n"))
#primefactors(n)
a = 3
b = 3


x = np.arange(a*b)

print(x)

first_step = dft_of_rows(x,a,b)
cmatrix_multiplied = calculate_multiply_twidles(first_step,a,b)
final_matrix = DFT_of_collumns(cmatrix_multiplied,a,b)



scipy_fft = calculate_sci_fft(x,a,b)


finalCT = np.array(final_matrix).T.reshape(len(x),1)
print(finalCT)


########################################################


print('\n\n\n\n\n\n\n')


plt.stem(abs(scipy_fft), markerfmt ='D')
plt.stem(abs(finalCT),'r')
plt.legend(['cooley', 'scipy'])

plt.show()




