'''
This will be our linear regression model, and here we will be splitting our dataset,
training the model and returning the accuracy and loss while writing everything to
our config file
'''
import pandas as pd
import numpy as np
import pca 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split


#Both the next functions are in case of a Linear Regression to compare the accuracy

#in our example, Gradient Boosting Regressor gives a 82% accuracy
def train_GBR(X, y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 150)
	
	# print(cols)
	# reg = LinearRegression()

	reg = GradientBoostingRegressor()

	reg.fit(X_train, y_train)

	print('The accuracy provided by the Gradien Boosting Algorithm is: ' + str(reg.score(X_test, y_test)))

	return reg.score(X_test, y_test)

#in our example, Linear regression gives a 54% accuracy
def train_LR(X, y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 150)

	reg = LinearRegression()

	reg.fit(X_train, y_train)

	print('The accuracy provided by the Linear Regression Algorithm is: ' + str(reg.score(X_test, y_test)))

	return reg.score(X_test, y_test)

#this is our sigmoid function that will serve as an activation function for our NN
def Sigmoid(z):
  return (1 / (1 + np.exp(-z.astype(float))))
