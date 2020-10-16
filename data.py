import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVR
from mylinearregression import *
from time import time


# -- Functions
def compute_linreg_numpy(x, y):
    x_ = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(x_, y, rcond=None)[0]
    return a, b

def compute_linreg_scipy(x, y):
    res = stats.linregress(x, y)
    return res[0], res[1]

def compute_linreg_sklearn(x, y):
    return LinearRegression().fit(x, y)

def compute_linereg_svr(x, y):
    return LinearSVR().fit(x, y)


# -- Run
# TODO GROS BORDEL, envisager une classe ?
car_data = pd.read_csv('data/carData.csv')
time_linreg = pd.DataFrame(columns=['msecs'])
fittedline ={}

time_start = time()
fittedline['numpy'] = compute_linreg_numpy(car_data['Year'], car_data['Selling_Price'])
time_linreg.loc['numpy'] = (time() - time_start) * 1000.

time_start = time()
fittedline['scipy'] = compute_linreg_scipy(car_data['Year'], car_data['Selling_Price'])
time_linreg.loc['scipy'] = (time() - time_start) * 1000.

time_start = time()
linreg = compute_linreg_sklearn(car_data['Year'].values.reshape(car_data['Year'].shape[0], 1), car_data['Selling_Price'])
fittedline['sklearn'] = (linreg.coef_[0], linreg.intercept_)
time_linreg.loc['sklearn'] = (time() - time_start) * 1000.

time_start = time()
linregsvr =  compute_linereg_svr(car_data['Year'].values.reshape(car_data['Year'].shape[0], 1), car_data['Selling_Price'])
fittedline['sklearn.svr'] = (linregsvr.coef_[0] if linregsvr.coef_.size == 1 else linregsvr.coef_, linregsvr.intercept_)
time_linreg.loc['sklearn.svr'] = (time() - time_start) * 1000.

mlr = MyLinearRegression()
time_start = time()
fittedline['MyLinearRegression'] = mlr.fit(car_data['Year'], car_data['Selling_Price'])
time_linreg.loc['MyLinearRegression'] = (time() - time_start) * 1000.

car_data_transcat = pd.get_dummies(data=car_data, columns=['Transmission'])
multivariate_reg = compute_linreg_sklearn(car_data_transcat[['Year', 'Kms_Driven']], car_data['Selling_Price'])
#fittedline['multivariate'] = (multivariate_reg[0][1], multivariate_reg[1])
print('Multivariate: ', multivariate_reg)

#test_multi_my = mlr.fit(car_data_transcat[['Year', 'Kms_Driven', 'Transmission_Automatic', 'Transmission_Manual']], car_data['Selling_Price'])
#print('Test multi my: ', test_multi_my)

print("Fitted Line:", fittedline)
