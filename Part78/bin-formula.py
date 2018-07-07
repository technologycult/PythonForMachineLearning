'''
Session # 78

Topic to be covered - Binning with Python based on a Mathematical Formula
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Salary.csv')

plt.hist(df['ApplicantIncome'])
plt.show()
####################################

no_of_bins = int(np.sqrt(len(df)))

plt.hist(df['ApplicantIncome'],no_of_bins)
plt.show()




