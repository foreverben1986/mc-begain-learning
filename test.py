from sympy import *
import numpy as np
x1 = symbols('x1')
y = symbols('y')
theta0, theta1 = symbols('theta0 theta1')
H = theta1 * x1 + theta0
J = (H - y)**2

JDotTheta1=J.diff(theta1)
JDotTheta2=J.diff(theta0)

print(JDotTheta1)
print(JDotTheta2)
# print(f(2,1))
# print(f(2,1).diff(x))