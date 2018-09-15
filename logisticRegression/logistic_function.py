import numpy as np

dValue = 1e-8
def logisticFunction(data):
    xData = buildXFromData(data)
    yData = buildYFromData(data)
    theta0 = 1
    theta1 = 1
    ###################### METHOD 1 START ####################
    while True:
        likehoodDx0Sum = 0
        likehoodDx1Sum = 0
        theta0Old = theta0
        theta1Old = theta1
        for i in (0, len(xData) - 1):
            likehoodDx0Sum = likehoodDx0Sum + likehoodDx(yData[i], xData[i][0], xData[i][1], xData[i][0], theta0, theta1)
        theta0 = theta0 + 20 * likehoodDx0Sum

        for i in (0, len(xData) - 1):
            likehoodDx1Sum = likehoodDx1Sum + likehoodDx(yData[i], xData[i][0], xData[i][1], xData[i][1], theta0, theta1)
        theta1 = theta1 + 20 * likehoodDx1Sum

        theta0Delta = theta0 - theta0Old
        theta1Delta = theta1 - theta1Old
        temp = theta0Delta * theta0Delta + theta1Delta * theta1Delta
        print "theta0: %s" % (theta0)
        print "theta1: %s" % (theta1)
        print "sum0: %s" % (likehoodDx0Sum)
        print "sum1: %s" % (likehoodDx1Sum)
        print "------------------------"
        if (temp < 0.000000000001):
            break

    print(theta0)
    print(theta1)
    ###################### METHOD 1 END ####################

    ###################### METHOD 2 START ####################
    ###################### METHOD 2 END ####################

    # gradP = Matrix(derive_by_array(loglikehood, thetaList))
    # hessenP = Matrix(hessian(loglikehood, thetaList)) 
    # gradPSum = None
    # hessenPSum = None

def buildXFromData(data):
    result = []
    result = map(lambda x: [1, x[:2][0]], data)
    return result

def buildYFromData(data):
    result = []
    result = map(lambda x: x[-1], data)
    return result
    
def hx(x0, x1, theta0, theta1):
    temp = np.exp(-x0 * theta0 - x1 * theta1)
    temp = max(temp, 1e-15)
    return 1/(1 + temp)

#
# (y−hθ(x))xj
#
def likehoodDx(y, x0, x1, dx, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return (y - temp) * dx

def likehoodD2x(y, x0, x1, dx, theta0, theta1):
    tempExp = np.exp(-x0 * theta0 - x1 * theta1) 
    tempExp = max(tempExp, 1e-15)
    return -1 * dx**2 * tempExp / ((1 + tempExp) **2)