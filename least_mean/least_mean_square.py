from sympy import *
import numpy as np

alpha = 1e-4
dValue = 1e-8
def executeRepeat(data):
    y = symbols('y')

    i = 1
    factors = []
    variables = []
    factors.append(symbols('theta0'))
    variables.append(symbols('x0'))
    print(data[0])
    for col in data[0]:
        factors.append(symbols('theta' + str(i)))
        variables.append(symbols('x' + str(i)))
        i = i + 1

    factors.pop()
    variables.pop()

    factorsM = np.array(factors) 
    variablesM = np.array(variables)

    H = factorsM.dot(variablesM)
    J = (H - y)**2
    print(J)

    variables.append(y)
    dataMapList = __dataHandle__(data, variables)

    # __optimize2__(J, factors[0], factors[1], data, variables[1], y)
    return __optimize__(J, dataMapList, factors, variables)

def __dataHandle__(data, variables):
    dataMapList = []
    for dataItem in data:
        dataItemMap = {}
        dataItemMap[variables[0]] = 1
        for i in range(1, len(variables)):
            dataItemMap[variables[i]] = dataItem[i - 1]
        dataMapList.append(dataItemMap)
    return dataMapList



def __optimize__(formula, dataMapList, factors, variables, factorsValues=None):
    if factorsValues == None:
        factorsValues = {}
        for i in range(0, len(factors)):
            factorsValues[factors[i]] = np.random.randint(1, 20)
    
    newFactorsValues = factorsValues.copy()
    #Repeat until convergence 
    while True:
        #for every j
        for i in range(0, len(factors)):
            # alpha * cigema()
            cigema = 0
            cigema2 = 0
            r = formula.diff(factors[i])
            rr = r.diff(factors[i])
            r = r.subs(newFactorsValues)
            rr = rr.subs(newFactorsValues)
            for dataMap in dataMapList:
                cigema = cigema + r.subs(dataMap)
                cigema2 = cigema2 + rr.subs(dataMap) 
            # newFactorsValues[factors[i]] = newFactorsValues[factors[i]] - alpha * cigema
            newFactorsValues[factors[i]] = newFactorsValues[factors[i]] - cigema/cigema2
        newFactorValuesM = np.array(newFactorsValues.values())
        factorsValuesM = np.array(factorsValues.values())
        print(newFactorsValues.values())
        temp = np.sum(np.square(newFactorValuesM-factorsValuesM))
        if (temp < dValue):
            break
        else:
            factorsValues = newFactorsValues.copy()
    print(newFactorsValues.values())
    return newFactorsValues