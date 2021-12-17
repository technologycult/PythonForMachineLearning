'''

Python for Machine Learning - Session # 100

Topic to be covered - Simple Imputer 

a. Imputing with Mean values

b. Imputing with Median Values

c. Imputing with Mode Values

d. Imputing with Constant Values

'''

from sklearn.preprocessing import Imputer

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df = pd.read_csv('diabetes1.csv')

###########################################################################

df2 = pd.DataFrame()

# task No 1
df2['col'] = [75,88,np.nan,94,168,np.nan,543]

mean_imputer = SimpleImputer(strategy='mean')

df2.iloc[:,:] = mean_imputer.fit_transform(df2)

# task No 1
df2=pd.DataFrame()
df2['col'] = [75,88,np.nan,94,168,np.nan,543]

median_imputer = SimpleImputer(strategy='median')

df2.iloc[:,:] = median_imputer.fit_transform(df2)

# Task No 3
df2=pd.DataFrame()
df2['col'] = [75,88,np.nan,94,168,220,543]

median_imputer = SimpleImputer(strategy='median')

df2.iloc[:,:] = median_imputer.fit_transform(df2)
print(df2)

# Task No 4
df2=pd.DataFrame()
df2['col'] = [75,88,np.nan,94,168,np.nan,543]

mode_imputer = SimpleImputer(strategy='most_frequent')

df2.iloc[:,:] = mode_imputer.fit_transform(df2)
print(df2)

# Task No 5
df2=pd.DataFrame()
df2['col'] = [75,88,np.nan,94,94,np.nan,543]

mode_imputer = SimpleImputer(strategy='most_frequent')

df2.iloc[:,:] = mode_imputer.fit_transform(df2)
print(df2)

# Task No 6
df2=pd.DataFrame()
df2['col'] = [75,88,np.nan,94,94,np.nan,543]

constant_imputer = SimpleImputer(strategy='constant',fill_value=100)

df2.iloc[:,:] = constant_imputer.fit_transform(df2)
print(df2)

#####################################################################

# Task No 7
# Impute with Mean

df_mean = df.copy(deep=True)

mean_imputer = SimpleImputer(strategy='mean')
df_mean.iloc[:,:] = mean_imputer.fit_transform(df_mean)
print(df_mean.isnull().sum())

# Task No 8
# Impute with Median

df_median = df.copy(deep=True)

median_imputer = SimpleImputer(strategy='median')
df_median.iloc[:,:] = median_imputer.fit_transform(df_median)
print(df_median.isnull().sum())



# Task No 9
# Impute with Median

df_mode = df.copy(deep=True)

mode_imputer = SimpleImputer(strategy='most_frequent')
df_mode.iloc[:,:] = mode_imputer.fit_transform(df_mode)
print(df_mode.isnull().sum())


# Task No 10
# Impute with Median

df_constant = df.copy(deep=True)

constant_imputer = SimpleImputer(strategy='constant',fill_value=48)
df_constant.iloc[:,:] = constant_imputer.fit_transform(df_constant)
print(df_constant.isnull().sum())

# Task No 11
# Impute different columns with different strategy

df3 = df.copy(deep=True)

df3.iloc[:,1] = mean_imputer.fit_transform(df3.iloc[:,1].values.reshape(-1,1))

df3.iloc[:,2] = median_imputer.fit_transform(df3.iloc[:,2].values.reshape(-1,1))

df3.iloc[:,3] = mode_imputer.fit_transform(df3.iloc[:,3].values.reshape(-1,1))

df3.iloc[:,4] = constant_imputer.fit_transform(df3.iloc[:,4].values.reshape(-1,1))
df3.iloc[:,5] = constant_imputer.fit_transform(df3.iloc[:,5].values.reshape(-1,1))


#############
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df2 = pd.DataFrame()

# task No 1
df2['col'] = [75,88,np.nan,94,168,np.nan,543]

mean_imputer = SimpleImputer(strategy='mean',missing_values =np.nan)

mean_imputer = SimpleImputer(strategy='mean',missing_values ='nan')













































































