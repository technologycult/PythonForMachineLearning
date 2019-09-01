'''

Polynomial Linear Regression using Scikit Learn
'''

#y = 9450x + 25792
#y = 16.393x2 + 9259.3x + 26215
#y = -122.92x3 + 2099.4x2 - 718.71x + 38863
#y = 4.9243x4 - 236.59x3 + 2979.9x2 - 3314.2x + 41165
#y = 15.006x5 - 430.13x4 + 4409.7x3 - 19368x2 + 43652x + 8315


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('SalaryData_Train.csv')

features = df.iloc[:,0:1].values
labels = df.iloc[:,1:2].values

#plt.scatter(df_train['YearsExperience'], df_train['Salary'])
plt.scatter(features,labels)
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary V/s Years of Experience')
plt.show()



#Step 6  - Sampling
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    labels,
                                                    test_size=0.33,
                                                    random_state=0)

# Create the REgression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# Create The Polynomial Features

from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=3)

x_poly = poly_reg.fit_transform(features)
regressor.fit(x_poly,labels)

# TEst the model 
y_pred = regressor.predict(poly_reg.fit_transform(X_test))

# Calculate the Accuracy

print('Polynomial Linear Regression Accuracy:',regressor.score(poly_reg.fit_transform(X_test),y_test))

for i in range(1,6):
    poly_reg = PolynomialFeatures(degree=i)
    x_poly = poly_reg.fit_transform(features)
    regressor.fit(x_poly,labels)
    print('Degree of Equation :', i)
    print('Coefficient :', regressor.coef_)
    print('Intercept :', regressor.intercept_)
    print('Accuracy Score:', regressor.score(poly_reg.fit_transform(X_test),y_test))
































