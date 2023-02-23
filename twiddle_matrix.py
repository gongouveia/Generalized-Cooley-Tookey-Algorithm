


import numpy as np


# converts the number to a signed binary number 
def convert_to_binary(value, number_of_bits = 24):

    if value <0:
        signed_value = "1"
    else:
        signed_value = "0"
    return  signed_value + str(bin(int(round(abs(value),3)*(2**12-1) )).zfill(number_of_bits-1)).replace("b","0").replace("-","")


def create_twiddle_std_logic_values(row_length,collumn_length):	
    N = row_length*collumn_length
    twiddle_code = "CONSTANT twiddle_matrix : MATRIX :=\n ("
    for i in np.arange(0,collumn_length):
        twiddle_code += "("
        for k in np.arange(0,row_length):
            num = np.exp(-2j*i*k*np.pi/N)
            #print(num)
            twiddle_code += "(\"" +convert_to_binary(num.real)+ "\",\"" + convert_to_binary(num.imag).replace("(", "") + "\")"
            #print(float_bin(round(num.real,4),8))
            #twiddle_code += '('+float_bin(xx , 8)
            if k == row_length-1:
                twiddle_code += "),\n"
            else:
                twiddle_code += ","              
    twiddle_code += ")"
    s = list(twiddle_code)
    s[-3] = ''
    twiddle_code = "".join(s)
    twiddle_code += ";"
    print(twiddle_code)

# Computes the DFT factors of a N size vector
def dft_factors(N):
    """ Obtem os valores das constantes"""
    X = np.zeros(N, dtype=complex)
    twiddle_n   =  []
    for k in range(N):
        for n in range(N):
            twiddle_n.append(np.exp(-2j * np.pi * k * n / N))
        #    print(np.exp(-2j * np.pi * k * n / N))
        #print('\n')
    return twiddle_n

# reshapes data
def format_data_properly(X, N):
    X = np.array(X).reshape(N, N)
    return X

def row_dft_collumn_factors(X, row_or_collumn): 
    twiddle_code = f"\n\nCONSTANT {row_or_collumn}_matrix_values : {row_or_collumn.upper()}_MATRIX :=\n (("
    for row in X:
        for num in row:
            twiddle_code += ",(\"" +convert_to_binary(num.real)+ "\",\"" + convert_to_binary(num.imag).replace("(", "") + "\")"
        twiddle_code += "),\n("
    twiddle_code += ");"
    print(twiddle_code.replace(",\n();",");").replace("(,(","(("))


# Final method to compute the tf of the rows and collumns
def row_or_collumn(N, row_or_collumn = "row"):
    X = dft_factors(N)
    X = format_data_properly(X,N)
    row_dft_collumn_factors(X,row_or_collumn)



create_twiddle_std_logic_values(4,3)


N_row = 3
row_or_collumn(N_row, "row")


N_collumn = 4
row_or_collumn(N_collumn, "collumn")


print(len("000000000000111111111111"))