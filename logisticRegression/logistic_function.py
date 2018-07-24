from sympy import MatrixSymbol, Matrix, symbols, exp, pprint
from sympy.tensor.array import derive_by_array
import numpy as np

X = MatrixSymbol('X', 3, 1)
THETA = MatrixSymbol('THETA', 3, 1)
def logisticFunction(data):
    pprint(Matrix(X.T).tolist()[0])
    xList = Matrix(X.T).tolist()[0]
    p = formulaP()
    gradP = Matrix(derive_by_array(p, xList))
    pprint(gradP)
    

def formulaP():
    l = symbols('l')
    z = X.T*THETA
    p = 1/(1 + exp(-l))
    p = p.subs(l, Matrix(z).trace())
    return p

    