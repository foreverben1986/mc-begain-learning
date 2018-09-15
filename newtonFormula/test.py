import numpy as np
import functools

def hx(x0, x1, theta0, theta1):
    temp = np.exp(-x0 * theta0 - x1 * theta1)
    temp = max(temp, 1e-15)
    print(temp)
    print(1/(1 + temp))
    return 1/(1 + temp)

def likehoodDx(y, x0, x1, dx, theta0, theta1):
    temp = hx(x0, x1, theta0, theta1)
    return (y - temp) * dx

# likehoodDxPartial = functools.partial(likehoodDx, y=1, x0=0.2, x1=50, dx=50)
# likehoodDxPartial2 = functools.partial(likehoodDx, y=1, x0=0.2, x1=50, dx=50)
print(3 ** 3)
    

