# %%
import numpy as np
# %%
# defininado a matrix Cnot
Cnot = np.array([[1, 0, 0, 0],[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
# %%
#Vai receber o tamanho da matrix qubit
# number = int(input())
number = 3
qubit = 2**number

print(qubit)
# %%
matrix_outp = np.arange(8, 8)
# %%
