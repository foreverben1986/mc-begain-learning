import numpy as np
import lib.linearRegression_data_read as xlsR

data = xlsR.readXls("data1.xlsx","data1")
mM = np.array(data)
mX = mM[:,:2]
mY = mM[:,2]
mX0 = np.ones(mX.shape[0])
mX = np.c_[mX0,mX]
xTX  = np.transpose(mX).dot(mX)
xTXInv = np.linalg.inv(xTX)
print(xTXInv.dot(mX.T).dot(mY))