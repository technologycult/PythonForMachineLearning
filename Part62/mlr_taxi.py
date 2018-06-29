"""
Topic to be Covered - Multivariate Linear Regression

@author: aly
"""
'''

#Step 1 - Import the necessary libraries and the dataset

#Step 2 - Plot the Seaborn Pairplot

#Step 3 - Plot the Seaborn Heatmap

#Step 4 - Extract the Features and Labels

#Step 5 - Cross Validation (train_test_split)

#Step 6 - Create the Linear Model (LinearRegression)

#Step 7 - Interpreting the Coefficient and the Intercept

#Step 8 - Predict the output

#Step 9 - Predict the Score (% Accuracy)

#Step 10- Verification of the Predicted Value

#Step 11- Calculate the MSE and RMSE

'''
'''

y = m*x + c

y = b0*x0 + b1*x1 + b2*x2 + b3*x3 + ... + bn*xn

y = b0 + b1*x1 + b2*x2 + b3*x3 + ... + bn*xn

Price per week    
Population of city    
Monthly income of riders    
Average parking rates per month
Number of weekly riders    

'''


#Step 1 - Import the necessary libraries and the dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('taxi.csv')

#Step 2 - Plot the Seaborn Pairplot
sns.pairplot(df)

#Step 3 - Plot the Seaborn Heatmap
sns.heatmap(df.corr(),linewidth = 0.2, vmax=1.0, square=True, linecolor='red',annot=True)

#Step 4 - Extract the Features and Labels

features = df.iloc[:,0:-1].values
labels = df.iloc[:,-1].values

#Step 5 - Cross Validation (train_test_split)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features,labels,test_size=0.3,random_state=0)


#Step 6 - Create the Linear Model (LinearRegression)
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train,y_train)

#Step 7 - Interpreting the Coefficient and the Intercept
y_pred = regressor.predict(X_test)

#Step 8 - Interpreting the Coefficient and the Intercept

print(regressor.coef_)
print(regressor.intercept_)

#Step 9 - Predict the Score (% Accuracy)

print('Train Score :', regressor.score(X_train,y_train))
print('Test Score:', regressor.score(X_test,y_test))


#Step 10- Verification of the Predicted Value

#y = b0 + b1*x1 + b2*x2 + b3*x3 + ... + bn*xn

y_output0 = regressor.intercept_ + regressor.coef_[0]*X_test[0][0] + regressor.coef_[1]*X_test[0][1] + regressor.coef_[2]*X_test[0][2] + regressor.coef_[3]*X_test[0][3] 

y_output1 = regressor.intercept_ + regressor.coef_[0]*X_test[1][0] + regressor.coef_[1]*X_test[1][1] + regressor.coef_[2]*X_test[1][2] + regressor.coef_[3]*X_test[1][3] 

#Step 11- Calculate the MSE and RMSE

from sklearn import metrics

print('MSE :', metrics.mean_squared_error(y_test,y_pred))

print('RMSE :', np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

###############################################################################
X1 = [[80, 1770000, 6000, 85]]
out1 = regressor.predict(X1)