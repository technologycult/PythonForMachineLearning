'''
Contact - technologycult@gmail.com

github link - https://github.com/technologycult

Python for Machine Learning - Session # 95

Topic to be covered - Backend working Mechanism of how Sklearn Models/Functions/Methods

'''

from  sklearn import  datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score


iris=datasets.load_iris()

# Features
x=iris.data

# Labels
y=iris.target

# Cross Validation
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)

# Decision Tree Classifier
classifier=tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)

#Prediction
predictions=classifier.predict(x_test)

# Accuracy
print(accuracy_score(y_test,predictions))

###############################################################################

df = pd.DataFrame()

df['objects'] = dir(classifier)

list1= dir(classifier)

for i in list1:
    print("{0}.{1}".format(classifier, i))
    print('#--------------------------------#')



list2=[]
for att in dir(classifier):
    print(att, getattr(classifier, att))
    list2.append(getattr(classifier,att))
    print('---------------------------------------')
    
df['values'] = list2





















