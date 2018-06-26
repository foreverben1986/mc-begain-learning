import numpy as np

def linearEquation(a, b):
    x = np.random.uniform(-10, 10, 100)
    y = a * x + b
    return (x, y)

def linearEquationWithNoise(a, b):
    linearEquationResult = linearEquation(a, b)
    noise = np.random.uniform(-10,10,100)
    resultWithNoise = (linearEquationResult[0], linearEquationResult[1] + noise)
    return resultWithNoise