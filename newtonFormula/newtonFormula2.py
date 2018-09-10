from sympy import MatrixSymbol, Matrix, symbols, exp, pprint, log, hessian
from sympy.tensor.array import derive_by_array
import numpy as np

x = symbols('x')
y = symbols('y')
THETA = MatrixSymbol('THETA', 2, 1)
f = x**4 + 3*y**4 + x**2 + x**2*y**2 + x + 2 + y**2 + y**3 + y

gradP = Matrix(derive_by_array(f, [x,y]))
pprint(gradP)
hessenP = Matrix(hessian(f, [x,y])) 
pprint(hessenP)
thetaResult = Matrix([[1],[1]])
xyMap = {x:1, y:1}

while True:
    xOld = xyMap[x]
    yOld = xyMap[y]
    gradPTemp = gradP.subs(xyMap).evalf()
    hessenPTemp = hessenP.subs(xyMap).evalf()
    diff = hessenPTemp.inv() * gradPTemp
    xyMap[x] = xyMap[x] - Matrix(diff).tolist()[0][0]
    xyMap[y] = xyMap[y] - Matrix(diff).tolist()[1][0]

    xDelta = xOld - xyMap[x]  
    yDelta = yOld - xyMap[y]
    temp = xDelta * xDelta  + yDelta * yDelta 
    print(temp)
    if (temp < 0.00000000001):
        break

pprint(xyMap)