from sympy import *
import numpy as np

alpha = 1e-6
dValue = 1e-10
def executeRepeat(data):
    temp = 'x1'
    x1 = symbols(temp)
    y = symbols('y')
    theta0, theta1 = symbols('theta0 theta1')
    H = theta1 * x1 + theta0
    J = (H - y)**2
    # theta' = theta - alpha * J.diff(theta)
    # __optimize__(J, theta0, theta1)
    __optimize2__(J, theta0, theta1, data, x1, y)

def __optimize1__(formula, *theta):
    # theta' = theta + alpha * J.diff(theta)
    b = theta[0]
    print(b)
    r1 = b + 1 * formula.diff(b)
    r1F = lambdify(b, r1, 'numpy')
    # t1 = lambdify(param[1], r1F(2) ,'numpy')
    # print(t1(2))
    print(r1F(1))

def __optimize2__(formula, theta0, theta1, data, x1, y):
    r1 = formula.diff(theta1)
    print(r1)
    r1ByData = lambdify((x1, y), r1, 'numpy')
    print(r1ByData)
    # r2 = theta1 - 1 * r1
    result = r1ByData(data[0][0], data[0][1])
    for i in range(1, 99):
        result = result + r1ByData(data[i][0], data[i][1]) 
    __optimizePart3__(result, theta0, theta1)

def __optimizePart3__(formula, theta0, theta1):
    r = theta1 - alpha * formula
    print(r)
    r1ByTheta0 = lambdify(theta0, r, 'numpy')
    r1ByTheta0F = lambdify(theta1, r1ByTheta0(1), 'numpy')
    print(r1ByTheta0(100))
    __optimizePart4__(r1ByTheta0F, 1, 0)

def __optimizePart4__(formula, theta1, time):
    # temp = formula(theta1)
    # print(theta1 - temp)
    # if (abs(theta1 - temp) < 0.000000000001):
    #     print("end::::::::::")
    #     print(theta1)
    #     print(time)
    #     return theta1
    # else:
    #     time = time + 1
    #     print(time)
    #     return __optimizePart4__(formula, temp, time + 1)
    temp = formula(theta1)
    while True:
        print(time)
        time = time + 1
        if (abs(formula(temp) - temp) < dValue):
            print(temp)
            break
        else:
            temp = formula(temp)



    # r1ByTheta0 = lambdify(theta0, r1 ,'numpy')
    # r1ByTheta0F = lambdify(theta1, r1ByTheta0(2), 'numpy')
    # print(r1ByTheta0F(1))