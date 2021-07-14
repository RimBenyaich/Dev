'''
This function will be using the Principle Component Analysis to perform
Dimensionality Reduction on the dataset for every correlated features
'''
from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .datafr import getcols

def corr(df, tar):
	"""This function will be calculating the correlation of our features with the target"""
	return df[df.columns[:]].corr()[tar]


def pca(df, tar):
	"""This function will be transforming our dataset according to the Principal Component Analysis technique"""
	lst = [""]
	X, y = split(df, tar)
	lst = getcols(X)
	# we standarize our dataset here
	X_std = StandardScaler().fit_transform(X[lst])
	'''
	select the minimum number of components from the sorted list (descending order) 
	according to their respective explained variance values such that the amount of 
	variance that needs to be explained is greater than the percentage specified by 
	n_components
	'''
	# will return a number of components that describes 92% of the variance
	pca = PCA(.92)
	pca.fit(X_std)
	data = pca.transform(X_std)

	# this will display a chart of our components along with their variance
	per = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
	labels = [f'PC{x}' for x in range(1, len(per)+1)]
	plt.bar(x=range(1, len(per) + 1), height=per,
			tick_label=labels, color='darkorange')
	plt.ylabel('Percentage of Explained Variance')
	plt.xlabel('Principle Component')
	plt.title('Variance of each')
	# TODO : make image path unique
	plt.savefig('./UserInterface/static/images/foo.png')
	num = np.array(data)
	newd = pd.DataFrame(num)
	return pd.concat([newd, y], axis=1)


# This function will be performing Linear Discriminent Analysis on our df
# TODO: complete code
def LDA(df, tar):
	X, y = split(df, tar)
	ld = LinearDiscriminantAnalysis()
	ld.fit_transform(X, y)
	plt.figure()

# This function will be performing Factor Analysis on our df
# TODO: complete code
def FA(df, tar):
	X, y = split(df, tar)
	transformer = FactorAnalysis(n_components=7, random_state=0)


# this function will split our features from our prediction/target
def split(df, target):
	X = df.loc[:, df.columns != target]
	y = df.loc[:, df.columns == target]

	return X, y
