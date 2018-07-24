import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import lib.linearRegression_data_read as xlsR
import least_mean_square as lms
import sys

data = xlsR.readXls("data1.xlsx","data1")
print(lms.executeRepeat(data))
