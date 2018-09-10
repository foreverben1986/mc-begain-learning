from sympy import MatrixSymbol, Matrix, symbols, exp, pprint, log, hessian
from sympy.tensor.array import derive_by_array
import numpy as np

X = MatrixSymbol('X', 2, 1)
THETA = MatrixSymbol('THETA', 2, 1)
y = symbols('y')
dValue = 1e-8
def logisticFunction(data):
    xData = buildXFromData(data)
    yData = buildYFromData(data)
    xList = Matrix(X.T).tolist()[0]
    thetaList = Matrix(THETA.T).tolist()[0]
    p = formulaP()
    loglikehood = log(p**y * ((1-p)**(1-y)))
    # pprint(loglikehood)
    # pprint(Matrix(THETA).row(0).col(0).trace())

    ###################### METHOD 1 START ####################
    logDTheta0 = loglikehood.diff(Matrix(THETA).row(0).col(0).trace())
    logDTheta1 = loglikehood.diff(Matrix(THETA).row(1).col(0).trace())
    pprint(xData[0])
    pprint(logDTheta0.subs(X, Matrix(xData[0])))
    pprint(logDTheta1.subs(X, Matrix(xData[0])))
    ###################### METHOD 1 END ####################

    ###################### METHOD 2 START ####################
    ###################### METHOD 2 END ####################

    # gradP = Matrix(derive_by_array(loglikehood, thetaList))
    # hessenP = Matrix(hessian(loglikehood, thetaList)) 
    # gradPSum = None
    # hessenPSum = None

def formulaP():
    l = symbols('l')
    z = X.T*THETA
    p = 1/(1 + exp(-l))
    p = p.subs(l, Matrix(z).trace())
    return p

def buildXFromData(data):
    result = []
    result = map(lambda x: [[1], [x[:2][0]]], data)
    return result

def buildYFromData(data):
    result = []
    result = map(lambda x: x[-1], data)
    return result
    