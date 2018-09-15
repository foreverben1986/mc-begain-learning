from sympy import MatrixSymbol, Matrix, symbols, exp, pprint, log, hessian
from sympy.tensor.array import derive_by_array
import numpy as np

x = symbols('x')
y = symbols('y')

f = log(1/(1+exp(-50*x))) + log(1 - 1/(1+exp(50*x)))
# f = (1 -1/(1+exp(-0.0001*x)))*0.0001 + (0 - 1/(1+exp(0.0001*x)))*(-0.0001)
pprint(f.subs(x, 1.2e-1).evalf())
fdx = f.diff(x)
# fdy = f.diff(y)

fd2x = fdx.diff(x)
# fd2y = fdy.diff(y)

xP = 1

# yP = 1
# while True:
#     xPOld = xP
#     # yPOld = yP

#     fdxValue = fdx.subs({x:xP}).evalf()
#     # fdyValue = fdy.subs({x:xP, y:yP})
#     fd2xValue = fd2x.subs({x:xP}).evalf()
#     # fd2yValue = fd2y.subs({x:xP, y:yP})
#     # fdxValue = fdx.subs({x:xP})
#     # fd2xValue = fd2x.subs({x:xP})

#     # xP = xP - 0.001 * fdx.subs({x:xP, y:yP})
#     # xP = xP + 10000 * fdx.subs({x:xP}).evalf()
#     # yP = yP - 0.001 * fdy.subs({x:xP, y:yP})
#     xP = xP - fdxValue.evalf()/fd2xValue.evalf()
#     # yP = yP - fdyValue.evalf()/fd2yValue.evalf()

#     xDelta = xPOld - xP  
#     # yDelta = yPOld - yP
#     # temp = xDelta * xDelta  + yDelta * yDelta 
#     temp = xDelta * xDelta
#     print("xP:", xP)
#     print("delta:", temp)
#     print("fdxValue:", fdxValue)
#     print("fdx2Value:", fd2xValue)
#     # print(yP)
#     if (temp < 0.0000000001):
#         break

print(xP)
# print(yP)
