'''
Session # 77

Topic to be covered - Binning with Python
'''

import pandas as pd

df = pd.read_csv('Salary.csv')

bins = [0,10000,25000,50000,100000]

labels = ['low', 'medium', 'standard', 'high']

df['ApplicantIncome_bin'] = pd.cut(df['ApplicantIncome'],bins,labels)

print(pd.value_counts(df['ApplicantIncome_bin'],sort=False))

df['categories'] = pd.cut(df['ApplicantIncome'],bins,labels=labels)

df['categories'].value_counts()

df['categories'].value_counts().plot(kind='barh')