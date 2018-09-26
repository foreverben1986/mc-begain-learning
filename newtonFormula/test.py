import numpy as np
from sympy import *
import functools

def hx(x0, x1, theta0, theta1):
    temp = np.exp(-x0 * theta0 - x1 * theta1)
    temp = max(temp, 1e-15)
    return 1/(1 + temp)

#
#
def likehoodDx(y, x0, x1, dx, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return (y - temp) * dx

# #
# #
def likehoodD2x(y, x0, x1, dx, theta0, theta1):
    tempExp = np.exp(-x0 * theta0 - x1 * theta1) 
    tempExp = max(tempExp, 1e-15)
    return -1 * dx**2 * tempExp / ((1 + tempExp) **2)

def likehoodTo(y, x0, x1, dx, theta0, theta1):
    tempExp = np.exp(-x0 * theta0 - x1 * theta1) 
    tempExp = max(tempExp, 1e-15)
    return -1 * (y * (1 + tempExp) - 1) * (1 + tempExp) / (dx * tempExp)

def likehood2(y, x0, x1, dx, theta0, theta1):
    tempExp = np.exp(-x0 * theta0 - x1 * theta1) 
    tempExp = max(tempExp, 1e-15)
    return -1 * (1 + tempExp) / dx


    
result1 = likehoodDx(0, 1, 50, 1, 1 ,1)
result2 = likehoodD2x(0, 1, 50, 1, 1 ,1)
print(result1)
print(result2)
print(result1/result2)

