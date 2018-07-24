import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import lib.linearRegression_data_read as xlsR
import sys
import logistic_function as lf

data = xlsR.readXls("logisticRegressionData.xlsx","Sheet1")
x1A = []
x2A = []
x1B = []
x2B = []
for dataItem in data:
    if dataItem[2]==1:
        x1A.append(dataItem[0])
        x2A.append(dataItem[1])
    else:
        x1B.append(dataItem[0])
        x2B.append(dataItem[1])



# matplotlib.rcParams['axes.unicode_minus'] = True
# fig, ax = plt.subplots()
# ax.plot(x1A, x2A, 'o', x1B, x2B, 'x')
# ax.set_title('Using hyphen instead of Unicode minus')
# plt.show()
# ax = plt.subplots()

lf.logisticFunction(data)