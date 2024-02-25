# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xbDGxErhDWCjm2DN3jqHdmU1elK0xSGe
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the training dataset
train_dataset = pd.read_csv('train_dataset.csv')

# Plot histogram for CPU Cores
plt.hist(train_dataset['CPU cores'], bins=10, color='darkblue', edgecolor='black')
plt.xlabel('CPU Cores')
plt.ylabel('Number of Laptops')
plt.title('Distribution of Laptops by CPU Cores Train datset')
plt.show()

# Load the training dataset
train_dataset = pd.read_csv('test_dataset.csv')

# Plot histogram for CPU Cores
plt.hist(train_dataset['CPU cores'], bins=10, color='darkblue', edgecolor='black')
plt.xlabel('CPU Cores')
plt.ylabel('Number of Laptops')
plt.title('Distribution of Laptops by CPU Cores Test datset')
plt.show()



import pandas as pd

# Load your train dataset
train_dataset = pd.read_csv('train_dataset.csv')

# Creating a pivot table for laptop count by RAM Size and Hard Disk Size for the train dataset
train_table = pd.pivot_table(train_dataset, index='RAM size', columns='drive memory size (GB)', values='id', aggfunc='count', fill_value=0)

# Save the table to a CSV file if needed
train_table.to_csv('laptops_count_by_RAM_and_HardDisk_train.csv')

# Display the table
print(train_table)

# Load your test dataset
test_dataset = pd.read_csv('test_dataset.csv')

# Creating a pivot table for laptop count by RAM Size and Hard Disk Size for the test dataset
test_table = pd.pivot_table(test_dataset, index='RAM size', columns='drive memory size (GB)', values='id', aggfunc='count', fill_value=0)

# Save the table to a CSV file if needed
test_table.to_csv('laptops_count_by_RAM_and_HardDisk_test.csv')

# Display the table
print(test_table)



"""# New Section"""

residuals = y_test - y_pred
plt.scatter(y_pred, residuals, alpha=0.5)
plt.title('Residual Plot')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.axhline(y=0, color='r', linestyle='-')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Assuming X_train, y_train, X_test, and y_test are already defined
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_train)
model = LinearRegression()
model.fit(X_poly, y_train)
y_pred = model.predict(poly.fit_transform(X_test))
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print("R-squared for the trained model:", r2)
print("MSE for the trained model:", mse)






# Assuming train_dataset and test_dataset are the dataframes for the train and test datasets
train_dataset.to_csv('train_model_data.csv', index=False)
test_dataset.to_csv('test_model_data.csv', index=False)