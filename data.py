import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from mylinearregression import *
from time import time

car_data = pd.read_csv('data/carData.csv')
time_linreg = {}

def compute_linreg_numpy(x, y):
    x_ = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(x_, y, rcond=None)[0]
    return a, b

def compute_linreg_scipy(x, y):
    res = stats.linregress(x, y)
    return res[0], res[1]

def compute_linreg_sklearn(x, y):
    reg = LinearRegression().fit(x, y)
    return reg.coef_, reg.intercept_

fittedline ={}

time_start = time()
fittedline['numpy'] = compute_linreg_numpy(car_data['Year'], car_data['Selling_Price'])
time_linreg['numpy'] = time() - time_start

time_start = time()
fittedline['scipy'] = compute_linreg_scipy(car_data['Year'], car_data['Selling_Price'])
time_linreg['scipy'] = time() - time_start

time_start = time()
fittedline['sklearn'] = compute_linreg_sklearn(car_data['Year'].values.reshape(car_data['Year'].shape[0], 1), car_data['Selling_Price'])
time_linreg['sklearn'] = time() - time_start

mlr = MyLinearRegression()
time_start = time()
fittedline['MyLinearRegression'] = mlr.fit(car_data['Year'], car_data['Selling_Price'])
time_linreg['MyLinearRegression'] = time() - time_start
print(fittedline['MyLinearRegression'])

car_data_transcat = pd.get_dummies(data=car_data, columns=['Transmission'])
ans = compute_linreg_sklearn(car_data_transcat[['Year', 'Kms_Driven', 'Transmission_Automatic', 'Transmission_Manual']], car_data['Selling_Price'])
fittedline['multivariate'] = (ans[0][0], ans[1])

test_multi_my = mlr.fit(car_data_transcat[['Year', 'Kms_Driven', 'Transmission_Automatic', 'Transmission_Manual']], car_data['Selling_Price'])
#print('Test multi my: ', test_multi_my)

#print("Time:", time_linreg)
print("Fitted Line:", fittedline)
