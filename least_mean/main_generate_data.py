import lib.data_generation as data_generation
import lib.linearRegression_data_generate as xlsW

result = data_generation.linearEquationWithNoise(20, 10, 20)
xlsW.generateXls("data1.xlsx","data1",result)