import matplotlib.pyplot as plt
import data_generation
import linearRegression_data_generate as xlsW
import linearRegression_data_read as xlsR
import least_mean_square as lms
import sys

result = data_generation.linearEquationWithNoise(20, 1)
xlsW.generateXls("data1.xlsx","data1",result)
data = xlsR.readXls("data1.xlsx","data1")
print(lms.executeRepeat(data))



# plt.scatter(data[0], data[1])
# plt.xlim(-10, 10)
# plt.show()