'''
This function will be using the Principle Component Analysis to perform
Dimensionality Reduction on the dataset for every correlated features
'''
from sklearn.decomposition import FactorAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .datafr import getcols
from .datafr import getdt

#This function will be calculating the correlation of our features with the target
def corr(df, tar):
	return df[df.columns[:]].corr()[tar]

#This function will be transforming our dataset according to the Principal Component Analysis technique
def pca(df, tar):
	lst = [""]
	X, y = split(df,tar)
	lst = getcols(X)
	#we standarize our dataset here
	X_std = StandardScaler().fit_transform(X[lst])
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
	plt.bar(x = range(1, len(per) + 1), height = per, tick_label = labels, color='darkorange')
	plt.ylabel('Percentage of Explained Variance')
	plt.xlabel('Principle Component')
	plt.title('Variance of each')
	plt.savefig('./UserInterface/static/images/foo.png')
	num = np.array(data)
	newd = pd.DataFrame(num)
	finaldf = pd.concat([newd, y], axis = 1)

	return finaldf

#This function will be performing Linear Discriminent Analysis on our df 
def LDA(df, tar):
	lst = [""]
	X, y = split(df,tar)
	ld = LinearDiscriminantAnalysis()
	

#This function will be performing Factor Analysis on our df
def FA(df, tar):
	X, y = split(df,tar)
	transformer = FactorAnalysis(n_components=7, random_state=0)
	X_transformed = transformer.fit_transform(X)

#this function will split our features from our prediction/target
def split(df, target):
	X = df.loc[:, df.columns != target]
	y = df.loc[:, df.columns == target]
	
	return X, y