'''

Python for Machine Learning - Session # 94

Topic to be covered - Shuffle parameter in train_test_split()

'''

import numpy as np
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape(10,1), range(10)

''' Case 1 '''
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=None)

print('X_train :',X_train)
print('X_test  :', X_test)
print('y_train :', y_train)
print('y_test  :', y_test)

''' Case 1 '''
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)

print('X_train :',X_train)
print('X_test  :', X_test)
print('y_train :', y_train)
print('y_test  :', y_test)

''' Case 2 '''
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,shuffle=True)

print('X_train :',X_train)
print('X_test  :', X_test)
print('y_train :', y_train)
print('y_test  :', y_test)

''' Case 3 '''
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,
                                                    random_state=1)

print('X_train :',X_train)
print('X_test  :', X_test)
print('y_train :', y_train)
print('y_test  :', y_test)


''' Case 4 '''
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,shuffle=True,
                                                    random_state=None)

print('X_train :',X_train)
print('X_test  :', X_test)
print('y_train :', y_train)
print('y_test  :', y_test)


y = np.array([1,1,1,1,1,0,0,0,0,0])
''' Case 4 '''
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,shuffle=True,
                                                    stratify=y,random_state=None)

print('X_train :',X_train)
print('X_test  :', X_test)
print('y_train :', y_train)
print('y_test  :', y_test)

''' Case 6 '''
y = np.array([1,1,1,1,1,0,0,0,0,0])
''' Case 4 '''
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,shuffle=False,
                                                    stratify=y,random_state=None)

print('X_train :',X_train)
print('X_test  :', X_test)
print('y_train :', y_train)
print('y_test  :', y_test)
















