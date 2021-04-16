'''
This function will be using the Principle Component Analysis to perform
Dimensionality Reduction on the dataset for every correlated features
'''
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def PC(df, lab, pos):
	# if(pos == 'beginning'):
	# 	X = df.iloc[:,lab:].values
	# 	y = df.iloc[:,lab - 1].values #this is the prediction and the value doesn't change as they're integers
	# else:
	# 	X = df.iloc[:,:lab].values
	# 	y = df.iloc[:,lab - 1].values #does not change as they are integers

	X, y = split(df,lab, pos)


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

	# print(X_std)
	# print(len(X_std))

	#this will display a chart of our components along with their variance
	per = np.round(pca.explained_variance_ratio_* 100, decimals = 1)
	labels = ['PC' + str(x) for x in range(1, len(per) + 1)]

	plt.bar(x = range(1, len(per) + 1), height = per, tick_label = labels)
	plt.ylabel('Percentage of Explained Variance')
	plt.xlabel('Principle Component')
	plt.title('Variance of each')
	plt.show()

	num = np.array(data)
	# print(data)
	# newd = pd.Series(num.tolist())
	newd = pd.DataFrame(num)
	# print(type(newd))
	finaldf = pd.concat([newd, y], axis = 1)

	return finaldf
	

def split(df, lab, pos):
	if(pos == 'beginning'):
		X = df.iloc[:,lab:].values
		y = df.iloc[:,lab - 1] #this is the prediction and the value doesn't change as they're integers
	else:
		X = df.iloc[:,:lab].values
		y = df.iloc[:,lab - 1].values #does not change as they are integers

	return X, y