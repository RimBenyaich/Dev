'''
This file will serve in the validation of our downloaded file
The validation will be as: check file extension, check counter of files, number of missing
values, etc..
'''

import os
from os import path
import json
from pathlib import Path
from .files import get_data
import pandas as pd
from .datafr import readcsv
from .files import save_to_config_func

#this will be our main check function that will call all of the other ones and return a message
def checks(conf):
	img_dir = '/images'
	choice = get_data('choice', conf)
	directory = './' + get_data("project_name", conf)
	dir = os.path.exists(directory + img_dir)
	c = int(choice)
	# print(directory)
	dirList = os.listdir(directory)
	cnt = len(dirList)
	if(c == 1):
		if(dir):
			message = "An undeclared image folder was found!"
			return message
		if(cnt > 1):
			message = "There are too many files"
		elif(cnt == 0):
			message = "There are too few files"
		elif(cnt == 1):
			if(check_ext(directory, ".csv")):
				message = "check"
				df = readcsv(directory, 'none')
				linescnt = len(df)
				save_to_config_func(linescnt, "lines counter", conf)
				# print("JEJE")
				save_to_config_func(cnt, "files counter", conf)
				# print("JOJO")

			else:
				message = "There are files with undeclared extensions"
	else:
		message = "The chosen format does not match the downloaded files"
	# print("CBON")
	return message
	
		# if(c == 1 or c == 3 or c == 6 or c == 7):
		# if(c == 1):
		# 	if(dir):
		# 		message = "An undeclared image folder was found!"
		# 		return message
		# 	if(cnt > 1):
		# 		message = "There are too many files"
		# 	elif(cnt == 0):
		# 		message = "There are too few files"
		# 	elif(cnt == 1):
		# 		if(check_ext(directory, ".csv")):
		# 			message = "check"
		# 			df = readcsv(directory)
		# 			linescnt = len(df)
		# 			save_to_config_func(linescnt, "lines counter", conf)
		# 			save_to_config_func(cnt, "files counter", conf)
		# 		else:
		# 			message = "There are files with undeclared extensions"
		# else:
		# 	if(not(dir)):
		# 		message = "There is a missing image folder!"
		# 		return message
		# 	if(cnt > 1):
		# 		message = "There are too many files"
		# 	elif(cnt == 0):
		# 		message = "There are too few files"
		# 	elif(cnt == 1):
		# 		if(check_ext(directory, ".csv")):
		# 			message = "check"
		# 			df = readcsv(directory)
		# 			linescnt = len(df)
		# 			save_to_config_func(linescnt, "lines counter", conf)
		# 			save_to_config_func(cnt, "files counter", conf)
		# 		else:
		# 			message = "There are files with undeclared extensions"
		# return message

#this function will check the extension of the downloaded file
def check_ext(directory, ext):
	for filename in os.listdir(directory):
		# print(filename)
		p = Path(directory)
		q = p / filename
		if not filename.endswith(ext):
			if not q.is_dir():
				return False
	return True

#this function will check the missing values in every category and their datatype
def check_missing(conf):
	directory = './' + get_data("project_name", conf)
	df = readcsv(directory, 'none')
	res = df.isnull().sum()

	return res

#this function will return the count of missing values in all our dataset
def missingcount(conf):
	directory = './' + get_data("project_name", conf)
	df = readcsv(directory, 'none')
	s = df.isnull().sum().sum()

	return s