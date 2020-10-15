import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

car_data = pd.read_csv('data/carData.csv')

# -- Quick look-out
print(car_data)
print('----\nColumns:')
print(car_data.columns)
print('----\nDescribe:')
print(car_data.describe())

# -- Qualitative data description
print('----\nQualitative descriptions:')
print('Fuel Type', car_data['Fuel_Type'].unique())
print('Seller Type', car_data['Seller_Type'].unique())
print('Transmission', car_data['Transmission'].unique())

#-- Check for N/A
print('---\nCount NA:')
print(car_data.isna().sum())

# plt.scatter(
#     x=car_data['Year'],
#     y=car_data['Selling_Price'],
#     marker='+'
# )
# plt.xlabel('Year')
# plt.ylabel('Selling Price')
# plt.show()

sns.scatterplot(
    x='Year',
    y='Selling_Price',
    size='Kms_Driven',
    sizes=(2,200),
    hue='Fuel_Type',
    palette='Set1',
    data=car_data)
plt.show()
