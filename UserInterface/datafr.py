'''
This py file will have all the functions related to the pandas' dataframe
'''
import pandas as pd
import os
from .files import get_data
from .files import save_to_config_func
from sklearn.preprocessing import OneHotEncoder

#this function will read our csv from the given directory
def readcsv(directory, f):
	if(f == 'none'):
		for filename in os.listdir(directory):
			if filename.endswith('.csv'):
				df = pd.read_csv(directory + '/' + filename)
				return df
		return None
	else:
		d = directory + '/' + f
		df = pd.read_csv(d)
		return df

#this function will save the categories of our dataset in our config file as well
def get_columns(conf):
    directory = './' + get_data("project name", conf)
    df = readcsv(directory, 'none')
    lst = []
    for col in df:
      lst.append(col)
    
    save_to_config_func(lst, "categories", conf)

    return lst

#this function will get our columns from our df
def getcols(df):
	lst = []

	for col in df:
		lst.append(col)

	return lst

def get_mod(pref):
	if pref == 1:
		mod = "CNN"
	elif pref == 2:
		mod = "ANN"
	elif pref == 3:
		mod = "Linear Regression"
	elif pref == 4:
		mod = "Logistric Regression"
	else:
		mod = "Any"

def dropcols(items, df):
	for it in items:
		df.drop(it, axis = 1, inplace = True)
	
	return df

def getdt(df):
	dt = []
	for col in df.columns:
		dt.append(type(df[col][1]))
	
	return dt

def colcnt(df):
	cnt = 0
	for col in df.columns:
		cnt = cnt + 1
	
	return cnt

def determine(y):
	i = 1
	j = []
	s = set()
	for i in list(range(1, len(y), 1)):
		s.add(i)

	if(len(s) / len(y)) > 0.9:
		return "Regression"
	else:
		return "Classification"