import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import time
import matplotlib.pyplot as plt
import numpy as np  

"""
This code accepts two lines (x1,x2) and (x3,x4) on 
the x-axis and returns whether they overlap. 
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
"""

#Line coordinates
X1 = 5
X2 = 15
X3 = 10 
X4 = 25

"""
Here the coordinate will be sorted to determine the start and end of each line.
"""
#Line coordinates Sorted
Cord = sorted([X1, X2, X3 ,X4])
Cor_1 =sorted([X1, X2])
Cor_2 =sorted([X3, X4])

#Method 1 
"""
In this method, the code will create two lines taking into account the spatial spaces 
and then assigning ones where the lines exist and zeros where the lines do not exist. 
If the lines overlap in a vector index, thus the value of this vector index will be 2.
This code can be expanded for multiple lines in the x-axis coordinates.
"""
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
"""
 In this method, the code will create two lists. These two lists will contain the line 
 of the coordinates previously inputted. Then will cast has a set to check if any item 
 in the first line is contained in the second line. If the first line contains any value 
 to the other line, the code will print an overlap. This code is more straightforward than
 the previous one. However, in case that is more than one line, it needs to be rewritten. 
"""
st1 = time.time()

L1 = list(range(Cor_1[0],Cor_1[1]+1))
L2 = list(range(Cor_2[0],Cor_2[1]+1))
if set(L1).intersection(set(L2)):
  print('overlap')
et1 = time.time()
print('Execution time Method 2:', et1-st1, 'seconds')
