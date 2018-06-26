import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy import special, optimize

def funct1(x):
    r = np.random.uniform(-5,5,100);
    print(x);
    print(r);
    return (10*x+r) 


x = np.linspace(0, 10, 100);
plt.figure(figsize=(8,4));
plt.scatter(x,funct1(x))
plt.xlabel("Time(s)");
plt.ylabel("Volt");
plt.title("PyPlot First Example");
plt.ylim(-5, 150);
plt.legend();
plt.show();