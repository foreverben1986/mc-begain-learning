from sympy import *
import numpy as np
vector1 = np.array([83.0149353979650, 27.0279349449601])
vector2 = np.array([83, 27])
 
print(vector1)
print(vector2)
op2=np.linalg.norm(vector1-vector2)
print(op2)