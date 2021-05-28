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
		df = pd.read_csv('./' + f)
		return df

#this function will save the categories of our dataset in our config file as well
def get_columns(conf):
    directory = './' + get_data("project_name", conf)
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

# def getmissnum(dic):
# 	d = []

# 	for key in dic:


# def getdt(df):
# 	dt = df.dtypes

# 	return dt