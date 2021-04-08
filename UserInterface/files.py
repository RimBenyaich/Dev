import os 
import datetime
import json 

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

def save_to_config_func(data, categ, conf):
	f = open(conf)
	dt = json.load(f) 
	dt[categ] = data

	with open(conf, 'w') as fp:
		json.dump(dt, fp)

def get_conf_categ(categ, conf):
	f = open(conf)
	dt = json.load(f)

	return dt[categ]

def rename_conf(directory, conf, name):
	Current_Date = datetime.datetime.today().strftime ('%d_%b_%Y_%H_%M_%S')

	conf = conf + name
	conf = conf + '_' + Current_Date + '.json'

	return conf

def init_conf(conf):
	# print(os.getcwd())
	f = open('template.json',)
	js = json.load(f)

	with open(conf, 'w') as fp:
		json.dump(js, fp)
	


def get_files(directory, ext):
	names = []
	for file in os.listdir(directory):
		if(file.endswith(ext)):
			names.append(file)

	return names

