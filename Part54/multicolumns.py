# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 00:17:33 2018

@author: Imran
"""

import pandas as pd

df = pd.read_csv('train.csv')

f1 = df.iloc[:,0].values
f2 = df.iloc[:,3:7].values
f3 = df.iloc[9:14].values

df1 = pd.DataFrame(f1)
df2 = pd.DataFrame(f2)
df3 = pd.DataFrame(f3)


frames = [df1,df2,df3]

df4 = pd.concat(frames)