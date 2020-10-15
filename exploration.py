import pandas as pd

car_data = pd.read_csv('data/carData.csv')

# -- Quick look-out
print(car_data)
print('----\nColumns:')
print(car_data.columns)
print('----\nDescribe:')
print(car_data.describe())

# -- Check for N/A
print('---\nCount NA:')
print(car_data.isna().sum())
