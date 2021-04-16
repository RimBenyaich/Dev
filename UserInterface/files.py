'''
This file will be handling all operations about naming our main folder of data, and our
json file. It will also do all the saving and retrieving from the config file 
'''

import os 
import datetime
import json 
import pandas as pd

#this function will rename our csv file
def renaming(directory, ext):
	path, dirs, files = next(os.walk(directory))
	Current_Date = datetime.datetime.today().strftime ('%d_%b_%Y_%H_%M_%S')
	# print(len(files))
	for file in os.listdir(directory):
		if(file.endswith(ext)):
			src = (directory + "/" + file)
			name = file.split('.')[0]
			dst = (directory + "/" + name + '_' + Current_Date + ext)
			os.rename(src, dst)

	return len(files)

#this function will save all of the form data to our config file 
def save_to_config_form(request, form, conf):
	f = open(conf, 'r+')
	js = json.load(f)

	for key, value in form.cleaned_data.items():
		if value:
			if(isinstance(value, int)):
				js[key] = int(value)
			else:
				js[key] = value

	data = json.dumps(js, indent = 4)

	with open(conf, 'w') as outfile:
		outfile.write(data)

#this function will save to our config file everything calculated (file cnt, lines cnt, etc..)
def save_to_config_func(data, categ, conf):
	f = open(conf)
	dt = json.load(f) 
	dt[categ] = data

	with open(conf, 'w') as fp:
		json.dump(dt, fp)

#this function will get us the actual saved value within a specific item of the config
def get_data(categ, conf):
	f = open(conf)
	dt = json.load(f)

	return dt[categ]

#this function will serve to rename our config file for a certain user in a certain format
def rename_conf(directory, conf, name):
	Current_Date = datetime.datetime.today().strftime ('%d_%b_%Y_%H_%M_%S')

	conf = conf + name
	conf = conf + '_' + Current_Date + '.json'

	return conf

#this function will initialize our configuration file by loading in it our template
def init_conf(conf):
	# print(os.getcwd())
	f = open('template.json',)
	js = json.load(f)

	with open(conf, 'w') as fp:
		json.dump(js, fp)

#this function will return our config file name
def get_config(directory):
	for file in os.listdir(directory):
		if(file.endswith('.json')):
			if(not file.endswith('template.json')):
				return file 
