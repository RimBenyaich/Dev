'''
This function will be using the Principle Component Analysis to perform
Dimensionality Reduction on the dataset for every correlated features
'''
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def corr(df, tar):
	return df[df.columns[0:]].corr()[tar]

def PC(df, tar):
	X, y = split(df,tar)

	#we standarize our dataset here
	X_std = StandardScaler().fit_transform(X)
	'''
	select the minimum number of components from the sorted list (descending order) 
	according to their respective explained variance values such that the amount of 
	variance that needs to be explained is greater than the percentage specified by 
	n_components
	'''
	pca = PCA(.92) #will return a number of components that describes 92% of the variance
	pca.fit(X_std)
	data = pca.transform(X_std)

	#this will display a chart of our components along with their variance
	per = np.round(pca.explained_variance_ratio_* 100, decimals = 1)
	labels = ['PC' + str(x) for x in range(1, len(per) + 1)]

	plt.bar(x = range(1, len(per) + 1), height = per, tick_label = labels)
	plt.ylabel('Percentage of Explained Variance')
	plt.xlabel('Principle Component')
	plt.title('Variance of each')
	plt.show()

	num = np.array(data)
	newd = pd.DataFrame(num)
	finaldf = pd.concat([newd, y], axis = 1)

	return finaldf

#this function will split our features from our prediction/target
def split(df, tar):
	X = df.loc[:, df.columns != 'tar']
	y = df.loc[:, df.columns == 'tar']
	
	return X, y