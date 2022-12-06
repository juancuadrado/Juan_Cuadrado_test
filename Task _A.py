import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import time
import matplotlib.pyplot as plt
import numpy as np  

X1 = 5
X2 = 15
X3 = 10 
X4 = 25

Cord = sorted([X1, X2, X3 ,X4])
Cor_1 =sorted([X1, X2])
Cor_2 =sorted([X3, X4])

#Method 1 
st = time.time()
All_Line = np.array(range(Cord[0],Cord[3]+1))
L1  = np.zeros(np.size(All_Line))
L2  = np.zeros(np.size(All_Line))
L1[int(np.where(All_Line ==Cor_1[0])[0]):int(np.where(All_Line ==Cor_1[1])[0])+1]=1
L2[int(np.where(All_Line ==Cor_2[0])[0]):int(np.where(All_Line ==Cor_2[1])[0])+1]=1
Final = L1 + L2
if 2 in Final:
  print('overlap')

et = time.time()
print('Execution time Method 1:', et-st, 'seconds')


del L1, L2, All_Line, Final

#Method 2
st1 = time.time()

L1 = list(range(Cor_1[0],Cor_1[1]+1))
L2 = list(range(Cor_2[0],Cor_2[1]+1))
if set(L1).intersection(set(L2)):
  print('overlap')
et1 = time.time()
print('Execution time Method 2:', et1-st1, 'seconds')