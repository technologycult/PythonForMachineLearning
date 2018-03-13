'''
Topics to be covered - Polynomial Regression without sklearn

'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6])
y = np.array([0.2,1.1,1.3,1.2,2.1,1.9,2.5])

'''
Degree 1 - y = 0.3321x + 0.475

Degree 2 - y = -0.0179x2 + 0.4393x + 0.3857

Degree 3 - y = 0.0194x3 - 0.1929x2 + 0.8282x + 0.269

Degree 4 - y = -0.0087x4 + 0.124x3 - 0.5799x2 + 1.2688x + 0.2242

Degree 5 - y = 0.0129x5 - 0.2025x4 + 1.1358x3 - 2.7112x2 + 2.7536x + 0.1873

'''

plt.plot(x,y,'o')

coefint1 = np.polyfit(x,y,1)
coefint2 = np.polyfit(x,y,2)
coefint3 = np.polyfit(x,y,3)
coefint4 = np.polyfit(x,y,4)
coefint5 = np.polyfit(x,y,5)

print(coefint1)
print(coefint2)
print(coefint3)
print(coefint4)
print(coefint5)

plt.plot(x,y,'o')
plt.plot(x,np.polyval(coefint1,x),'black')
plt.plot(x,np.polyval(coefint2,x),'g')
plt.plot(x,np.polyval(coefint3,x),'r')
plt.plot(x,np.polyval(coefint4,x),'y')
plt.plot(x,np.polyval(coefint5,x),'c')


for i in range(1,6):
    print('Degree is ', i)
    p = np.polyfit(x,y,i)
    plt.plot(x,np.polyval(p,x), color='blue')
    plt.show()
    
###############################################################################
    
ypred = coefint2[0]*x*x + coefint2[1]*x + coefint2[2]

print('Predicted Values:', ypred)

print('Actual Values :', y)

###############################################################################


ypred = coefint1[0]*x + coefint1[1]
print(ypred)

print(y)

yresidual = y - ypred

Sumofresidual = sum(pow(yresidual,2))
SumofTotal = len(y) * np.var(y)
Rsquare = 1 - Sumofresidual/SumofTotal

print(Rsquare)


from scipy.stats import linregress
slope, intercept, r_value, p_value, str_err = linregress(x,y)
print(pow(r_value,2))















































    
    
    
    
    
    
    
    
    
    






