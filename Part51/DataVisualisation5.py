'''
Topics to be Covered -
1. Seaborn lmplot for plotting linear regression.
2. Generate a residual plot.
3. Generate a Scatter plot.
4. Plot a linear regression between the variables of iris dataset by specifing the hue.
5. Plot a linear regression between the variables of iris dataset grouped by row-wise.
6. Make a striplot of SL, SW and PL, PW grouped by Species.
7. Generate a swarmplot.
8. Generate a Violin plot
9. Generate a joint plot
10. Pairwise joint Distribution
11. Pairwise joint Distribution grouped by Species
12. Heatmap
13. Boxplot
14. kdeplot
15. Andrews Curve
16. Radviz.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv('iris.csv')

# 1. Seaborn lmplot for plotting linear regression.

sns.lmplot(x='SepalLength',y='SepalWidth',data=iris)
sns.lmplot(x='PetalLength',y='PetalWidth',data=iris)

# 2. Generate a residual plot.

sns.residplot(x = iris['SepalLength'], y =iris['SepalWidth'], color='red')
sns.residplot(x = iris['PetalLength'], y =iris['PetalWidth'], color='red')

# 3. Generate a Scatter plot.

plt.scatter(iris['SepalLength'], iris['SepalWidth'], label='iris', color='red',marker = 'o')
#plt.scatter(iris['SepalLength'], iris['SepalWidth'], label='iris', color='red',marker = 'o')

sns.regplot(x = iris['SepalLength'], y =iris['SepalWidth'], data = 'iris', color='red', label = 'Order 1', order=1)
sns.regplot(x = iris['SepalLength'], y =iris['SepalWidth'], data = 'iris', color='blue', label = 'Order 2', order=2)
sns.regplot(x = iris['SepalLength'], y =iris['SepalWidth'], data = 'iris', color='yellow', label = 'Order 3', order=3)


# 4. Plot a linear regression between the variables of iris dataset by specifing the hue.
sns.lmplot(x='SepalLength',y='SepalWidth',data=iris,hue='Species', palette='Set1')

# 5. Plot a linear regression between the variables of iris dataset grouped by row-wise.
sns.lmplot(x='SepalLength',y='SepalWidth',data=iris,row='Species')

# 6. Make a striplot of SL, SW and PL, PW grouped by Species.
plt.subplot(2,2,1)
sns.stripplot(x='Species',y='SepalLength',data=iris)

plt.subplot(2,2,2)
sns.stripplot(x='Species',y='SepalWidth',data=iris, jitter = True, size=4)

#7. Generate a swarmplot.
sns.swarmplot(x='Species', y = 'SepalWidth', data=iris)
sns.swarmplot(x='Species', y = 'SepalLength', data=iris)

#8. Generate a Violin plot
sns.violinplot(x='Species', y = 'SepalWidth', data=iris)

#9. Generate a joint plot
sns.jointplot(x='SepalLength', y = 'SepalWidth', data=iris)

#10. Pairwise joint Distribution
sns.jointplot(x='SepalLength', y = 'SepalWidth', data=iris, kind='resid')

#11. Pairwise joint Distribution grouped by Species

sns.pairplot(iris)
# Pairwise joint Distribution grouped by Species
sns.pairplot(iris,hue='Species',kind='reg')

# 12. Heatmap
sns.heatmap(iris.corr(),linewidth=0.3,vmax=1.0,square=True, linecolor='black',annot=True)

# 13 Boxplot
sns.boxplot(x='Species', y = 'SepalLength', data=iris)

# 14. Kdeplot
sns.FacetGrid(iris,hue='Species',size=4) \
   .map(sns.kdeplot,'SepalLength') \
   .add_legend()

# Andrews Curve
from pandas.tools.plotting import andrews_curves
andrews_curves(iris.drop("Id", axis=1), 'Species')

# radviz
from pandas.tools.plotting import radviz
radviz(iris.drop("Id", axis=1), 'Species')


































