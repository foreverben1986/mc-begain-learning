import numpy as np
from sympy import exp

dValue = 1e-8
eps = np.finfo(float).eps
def logisticFunction(data):
    xData = buildXFromData(data)
    yData = buildYFromData(data)
    theta0 = -0.00001
    theta1 = 0.00001
    i = 0

    thetaMatrix = np.matrix(np.array([[theta0], [theta1]]))
    loglikehoodSumResult = 0
    while True:
        i = i + 1
        likehoodDx0Sum = 0
        likehoodDx1Sum = 0
        likehoodD2x0Sum = 0
        likehoodD2x1Sum = 0
        theta0Old = theta0
        theta1Old = theta1

        likehoodHessian11Sum = 0 
        likehoodHessian12Sum = 0
        likehoodHessian21Sum = 0
        likehoodHessian22Sum = 0
    ###################### METHOD 1 START ####################
        # for i in range(len(xData)):
        #     likehoodDx0Sum = likehoodDx0Sum + likehoodDx(yData[i], xData[i][0], xData[i][1], xData[i][0], theta0, theta1)
        # theta0 = theta0 + 0.00001 * likehoodDx0Sum

        # for i in range(len(xData)):
        #     likehoodDx1Sum = likehoodDx1Sum + likehoodDx(yData[i], xData[i][0], xData[i][1], xData[i][1], theta0, theta1)
        # theta1 = theta1 + 0.00001 * likehoodDx1Sum

        # for i in range(len(xData)):
        #     likehoodSum = likehoodSum * likehood(yData[i], xData[i][0], xData[i][1], theta0, theta1)

        # theta0Delta = theta0 - theta0Old
        # theta1Delta = theta1 - theta1Old
        # temp = theta0Delta * theta0Delta + theta1Delta * theta1Delta
        # print "theta0: %s" % (theta0)
        # print "theta1: %s" % (theta1)
        # print "temp: %s" % (temp)
        # print "likehoodSum: %s" % (likehoodSum)
        # print "------------------------"
    ###################### METHOD 1 END ####################

    ###################### METHOD 2 START ####################
        thetaMatrixOld = thetaMatrix.copy()

        x0List = getX0(data) 
        x1List = getX1(data) 
        yList = getY(data) 
        gradient11 = likehoodDxSum(yList, x0List, x1List, x0List, theta0, theta1)
        gradient21 = likehoodDxSum(yList, x0List, x1List, x1List, theta0, theta1)
        likehoodD2xSum11 = likehoodD2xSum(yList, x0List, x1List, x0List, x0List, theta0, theta1)
        likehoodD2xSum21 = likehoodD2xSum(yList, x0List, x1List, x0List, x1List, theta0, theta1)
        likehoodD2xSum22 = likehoodD2xSum(yList, x0List, x1List, x1List, x1List, theta0, theta1)

        loglikehoodSumResultOld = loglikehoodSumResult  
        loglikehoodSumResult = loglikehoodSum(yList,x0List,x1List, theta0, theta1)
        g = np.array([[gradient11],[gradient21]]) 
        h = np.array([[likehoodD2xSum11, likehoodD2xSum21], [likehoodD2xSum21, likehoodD2xSum22]])
        h_inv = np.linalg.inv(h)
        delta = np.dot(h_inv, g)
        deltaTheta0 = delta[0][0]                                                              
        deltaTheta1 = delta[1][0] 
        theta0 = theta0 - deltaTheta0
        theta1 = theta1 - deltaTheta1
        temp = abs(loglikehoodSumResultOld - loglikehoodSumResult)
        print "g: %s" % g
        print "h_inv: %s" % h_inv
        print "theta0: %s" % theta0
        print "theta1: %s" % theta1
        print "loglikehoodSumResultOld: %s" % loglikehoodSumResultOld
        print "loglikehoodSumResult: %s" % loglikehoodSumResult
        print("------------------")
        
        # print(diffMatrix)
        # print(temp)
        # print(likehoodSum)
    ###################### METHOD 2 END ####################

        if (temp < 0.000000000001 or i == 20):
            break



    # gradP = Matrix(derive_by_array(loglikehood, thetaList))
    # hessenP = Matrix(hessian(loglikehood, thetaList)) 
    # gradPSum = None
    # hessenPSum = None

def getX0(data):
    result = []
    result = map(lambda x: 1, data)
    return np.array(result)

def getX1(data):
    result = []
    result = map(lambda x: x[:2][0], data)
    return np.array(result)

def getY(data):
    result = []
    result = map(lambda x: x[-1], data)
    return np.array(result)

def buildXFromData(data):
    result = []
    result = map(lambda x: [1, x[:2][0]], data)
    return result

def buildYFromData(data):
    result = []
    result = map(lambda x: x[-1], data)
    return result
    
def hx(x0, x1, theta0, theta1):
    temp1 = (-x0 * theta0 - x1 * theta1).astype("float_")
    temp = np.exp(temp1)
    result = 1/(1 + temp) 
    return np.array(map(mymap, result))

#
#
def likehoodDx(y, x0, x1, dx, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return (y - temp) * dx

# #
# #
def likehoodD2x(y, x0, x1, dx1, dx2, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return temp * (temp - 1) * dx1 * dx2

def loglikehoodSum(y, x0, x1, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return np.sum(y * np.log(temp) + (1-y) * np.log(1 - temp))

def likehoodDxSum(y, x0, x1, dx, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return np.sum((y - temp) * dx)

def likehoodD2xSum(y, x0, x1, dx1, dx2, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return np.sum(temp * (temp - 1) * dx1 * dx2)

def mymap(t):
    if t == 0:
        return t + eps
    elif t == 1:
        return t - eps
    else:
        return t
