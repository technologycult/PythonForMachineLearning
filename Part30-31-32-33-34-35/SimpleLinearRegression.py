'''

Topic to be covered - Simple Linear Regression

Scenario - 
We have the Years of Experience and the Salary with us. We will train the model
using LinearRegression from scikit Learn and predict the Salary.
'''

# Step 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2 - Load the dataset
df_train = pd.read_csv('SalaryData_Train.csv')

# Step 3
print(df_train.head())

# Step 4 - Visualisation

plt.scatter(df_train['YearsExperience'],df_train['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary in ???')
plt.title('Salary V/S Years of Experience')
plt.show()

# Step 5 - Feature Extraction

feature = df_train.iloc[:,:-1].values
labels = df_train.iloc[:,1].values

print('Shape of Feature:',feature.shape)
print('Shape of Labels:', labels.shape)

# Step 6 - Sample 

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(feature,
                                                    labels,
                                                    test_size = 0.3,
                                                    random_state=0)

# Step 7 - Create the Linear Regression Model

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

# step 8 - fit the regression (reg) model that we have prepared with train and
# test dataset in the sampling step

reg.fit(X_train,y_train)

plt.scatter(X_train,y_train,color='r')
plt.plot(X_train,reg.predict(X_train),color='b')
plt.show()

'''
y = mx + c 

m = slope

c = y-intercept
'''

# Slope
reg.coef_


# intercept
reg.intercept_


'''
y = m*x + c
'''
y = 9360.26128619*7.9 + 26777.391341197632


y_pred = reg.predict(X_train)

y_predtest = reg.predict(X_test)

#-------------------#

df_test = pd.read_csv('SalaryData_Test.csv')

feature_test = df_test.iloc[:,0].values

#sy_pred_featuretest = reg.predict(feature_test)

feature_test = feature_test.reshape(-1,1)

y_pred_featuretest = reg.predict(feature_test)


# Accuracy
print('Train Accuracy :', reg.score(X_train,y_train))
print('Test Accuracy :', reg.score(X_test,y_test))




#------------------------------------------#

'''
RSS - Residual sum of squares

MSE - Mean Squared Error

RMSE - Root Mean Squared Error

'''

RSS = ((y_test - y_predtest)**2).sum()

MSE = np.mean((y_test - y_predtest)**2)

RMSE = np.sqrt(MSE)

#------------------------------------------------#

''' RSquare and Adjusted RSquare '''

SS_Residual = sum((y_train - y_pred)**2)

SS_total = sum((y_train - np.mean(y_train))**2)

R_Square = 1 - (float(SS_Residual)) / SS_total

Adjusted_R_Square = 1 - ( 1- R_Square)*(len(y_train)-1)/ (len(y_train)-X_train.shape[1]-1)

#------------------------------------------------#

import statsmodels.api as sm
X1 = sm.add_constant(X_train)

result = sm.OLS(y_train,X1).fit()

print('R Square : ',result.rsquared)
print('Adjusted R Square: ',result.rsquared_adj)































































