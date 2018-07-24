import numpy as np

def linearEquation(a, b, c):
    x1 = np.random.uniform(-10, 10, 30)
    x2 = np.random.uniform(-10, 10, 30)
    y = a * x1 + b * x2 + c
    return (x1, x2, y)

def linearEquationWithNoise(a, b, c):
    linearEquationResult = linearEquation(a, b, c)
    noise = np.random.uniform(-10,10,30)
    resultWithNoise = list(linearEquationResult)
    resultWithNoise[-1] = resultWithNoise[-1] + noise

    return tuple(resultWithNoise)