'''

Topic to be covered - Detect Outliers using Elliptic Envelopes

'''


import pandas as pd
import numpy as np

from sklearn.covariance import EllipticEnvelope

dataset = pd.read_csv('Salary.csv')


X = np.array([[100,100],
              [1,1],
              [2,4],
              [5,6],
              [6,8]])

outlier = EllipticEnvelope(contamination=0.1)

outlier.fit(X)
prediction1 = outlier.predict(X)
print(prediction1)

#--------------------------------------#

features = dataset.iloc[:,[1,2]].values

outlier1 = EllipticEnvelope(contamination=0.1)

outlier1.fit(features)
prediction2 = outlier1.predict(features)

print(prediction2)

dataset['outliers'] = prediction2