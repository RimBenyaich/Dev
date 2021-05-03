'''
This py file will have all the functions related to the pandas' dataframe
'''
import pandas as pd
import os
from .files import get_data
from .files import save_to_config_func

#this function will read our csv from the given directory
def readcsv(directory):
	for filename in os.listdir(directory):
		if filename.endswith('.csv'):
			df = pd.read_csv(directory + '/' + filename)
			return df
	return None

#this function will save the categories of our dataset in our config file as well
def get_columns(conf):
    directory = './' + get_data("project_name", conf)
    df = readcsv(directory)
    lst = []
    for col in df:
      lst.append(col)
    
    save_to_config_func(lst, "categories", conf)

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