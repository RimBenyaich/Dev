import os

import pandas as pd
from django.shortcuts import render

from .check import check_missing, checks, missingcount
from .clean import handlemiss
from .datafr import colcnt, determine, dropcols, get_columns, getcols, readcsv
from .downloadfromgd import recurs_folders
from .files import (delete, get_config, get_data, init_conf, rename_conf,
					renaming, save_to_config_form, save_to_config_func)
from .forms import HomeForm, TransformForm
from .genform import gencleanform, generateform, genere
from .model import train_GBR, train_LR
from .Transform import FA, LDA, corr, pca, split
from .forms import CheckForm, DropFeat
from pprint import pprint

# from .models import DFModel
# https://drive.google.com/drive/u/0/folders/1SfNihWNYJQPsniZ-yjQN6lgl1sUYw6RL

conf = ''
img_dir = '/images'
path = ''
probtype = ''


# Here will be our home page
def UI(request):
	conf = 'config_'
	curr = os.getcwd() + '/'
	direct = curr + "downloadable/"
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():
			project_name = request.POST.get('project_name')
			url = request.POST.get('url')
			new_r = url.split('/')[-1]
			cnt = 0
			path = curr + project_name + '/'
			conf = rename_conf(direct, conf, project_name)
			cnt = recurs_folders(new_r, cnt, path + '/')
			renaming(path, '.csv')
			form.cleaned_data
			init_conf(conf)
			save_to_config_form(request, form, conf)
			return render(request, 'download.html', {'conf': conf})
	else:
		form = HomeForm()
	return render(request, 'home.html', {'form': form})


# Here, we will be checking the syntax and format of the file and check for any missing values
def checking(request):
	directory = os.getcwd()
	datat = {}
	d = directory + "/downloadable"
	message = ""
	dt = {}
	conf = get_config(d)
	message = checks(conf)

	if message != "check":
		delete(directory, d + "/" + conf)
		return render(request, 'notchecked.html', {'message': message})

	dire = './' + get_data("project name", conf)

	df = readcsv(dire)
	categs = get_columns(conf)
	nbMisingVals = missingcount(conf)
	dic = check_missing(conf)
	for key, value in dic.items():
		datat[key] = str(df.dtypes[key])
		if value > 0:
			dt[key] = str(df.dtypes[key])

	# datat : dictionnary of all cols (column_name : datatype)
	# dt : dictionary of cols with missing values (column_name : datatype)
	save_to_config_func(dt, 'missing values datatype', conf)
	save_to_config_func(datat, 'datatype', conf)

	# TODO: get rid of this
	out = gencleanform(dic, dt)
	genere(out)

	dfHead = df.head().to_html(
		float_format=lambda x: '{0:.2f}'.format(x) if pd.notnull(x) else x)
	dfCols = df.columns.to_list()
	if nbMisingVals == 0:
		form = CheckForm()
		print([attr for attr in dir(form) if not attr.startswith('__')])
		return render(request, 'checked.html', {'num': nbMisingVals, 'categs': categs, 'form': form, 'dataframe': dfHead, 'dfCols': dfCols})
	else:
		form = CheckForm()
		print([attr for attr in dir(form) if not attr.startswith('__')])
		cnt = len(categs)
		return render(request, 'checked.html', {'num': nbMisingVals, 'dic': dic, 'form': form, 'categs': categs, 'cnt': cnt, 'dt': dt, 'dataframe': dfHead, 'dfCols': dfCols})


# Here, we will be handling the missing values
def clean(request):
	curr = os.getcwd()
	d = curr + "/downloadable"
	conf = get_config(d)
	dic = []
	nums = {}
	categs = {}
	x = 0
	num = 0
	d = []
	if request.method == 'POST':
		form = CheckForm(request.POST)
		pprint(request.POST)
		if form.is_valid():
			# Here will be the for loop that will regroup our handling for each missing value
			dic = get_data("missing values datatype", conf)
			# print(dic)
			# print(len(dic))
			for key in dic:
				if dic[key] in ['float64', 'int64']:
					x = int(request.POST.get(key))
					d = {
						1: "Drop",
						2: "Mean",
						3: "Max",
						4: "Min"
					}
					nums[key] = d[x]
				else:
					categs[key] = int(request.POST.get(key))
					if x == 1:
						nums[key] = "Drop"
					elif x == 2:
						nums[key] = "Mode"
			target_column = request.POST.get('target')
			save_to_config_func(nums, 'handle missing numbers', conf)
			save_to_config_func(categs, 'handle missing categories', conf)
			directory = './' + get_data("project name", conf)
			num = get_data("lines counter", conf)
			save_to_config_func(target_column, 'prediction', conf)
			save_to_config_func(len(dic), 'values handled count', conf)
			df = handlemiss(nums, categs, directory)
			x = len(df[target_column].unique())
			newnum = len(dic)
			save_to_config_func(len(df), "lines counter after cleaning", conf)
			# here I'll need to generate the model for my df and save it there
			# X, y = split(df, target_column)
			# print(curr)
			# Here we will be transforming our categorical values
			obj_df = df.select_dtypes(include=['object']).copy()
			for col in obj_df:
				df[col] = df[col].astype('category')
				pd.get_dummies(df, columns=[col])

			# TODO separate the normal categories from datetime formats
			for col in df:
				if col == "date":
					x = df[col].str.len()
					if x[1] == 15:
						df[col] = df[col].str.slice(0, 8)
						df[col] = df[col].astype(int)
			correl = corr(df, target_column)
			# print(correl)
			newf = generateform(correl, target_column)
			genere(newf)
			df.to_csv(curr + '/downloadable/cleaned.csv', index=False)
			# generate(get_model_repr(df))
			form = DropFeat()
			return render(request, 'clean.html', {'form': form, 'conf': conf, 'num': newnum, 'corr': correl, 'target': target_column})
			# return HttpResponse(df.to_html())
	else:
		form = CheckForm()
	# checking(path, conf)
	return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form})


# In this section, we will be continuing the cleaning (dropping features selected by the user)
def cleancontinued(request):
	curr = os.getcwd()
	d = curr + "/downloadable/"
	conf = get_config(d)
	message = ""
	items = []
	categs = []
	cnt = 0
	df = readcsv(d)

	# I generated a form that has checkboxes depending on the correlation table
	if request.method == 'POST':
		categs = getcols(df)
		form = DropFeat(request.POST or None)
		for col in categs:
			if request.POST.get(col) == 'on':
				items.append(col)
				cnt += 1
		if cnt == 0:
			df.to_csv(curr + '/downloadable/fullycleaned.csv', index=False)
			if os.path.exists(curr + "/downloadable/cleaned.csv"):
				os.remove(curr + "/downloadable/cleaned.csv")
			message = "No columns will be dropped"

			form = TransformForm()
			help_text = ["PCA Aims to find components that account for maximum variance in the data (including error and within-variable variance). Unlike LDA, it does not  take into account class membership (i.e., unsupervised), and is used when such information is not available. Importantly, both LDA and PCA do not require any prior notion of how the variables are related among themselves, and the resulting components can not be interpreted in terms of an underlying construct",
						 "LDA identifies components (i.e., linear combination of the observed variables) that maximize class separation (i.e. between-class variance) when such prior information is available (i.e., supervised). E.g., you have a training set containing a variable specifying the class of each observation. ",
						 "FA Tries to uncover latent factors that account for the variance shared between the observed variables (thus excluding error and within-variable variance). Ideally, the resulting latent factors represent interpretable underlying constructs. FA should be used when you assume that an underlying causal model induces covariance between several observed variables. Consequently, unlike PCA and LDA, the observed variables are linear combinations of the estimated latent factors."]
			return render(request, 'cleancontinued.html', {'form': form, 'help_text': help_text, 'message': message, 'cnt': cnt})
		else:
			# We make changes on df aka drop the selected columns and return the new df
			save_to_config_func(items, 'columns to drop', conf)
			newdf = dropcols(items, df)
			# Haven't decided yet whether we should delete cleaned.csv and keep fullycleaned or keep them both
			newdf.to_csv(curr + '/downloadable/fullycleaned.csv', index=False)

			message = "The following were dropped: \n"
			form = TransformForm()

			return render(request, 'cleancontinued.html', {"items": items, "form": form, 'message': message, 'cnt': cnt})
	else:
		form = DropFeat()
		# df.to_csv('fullycleaned.csv', index = False)
		# if os.path.exists("cleaned.csv"):
		# 	os.remove("cleaned.csv")
		# message = "No columns will be dropped"
		# form = TransformForm()
	return render(request, 'clean.html', {"items": items, 'message': message, 'cnt': cnt})


def correlation(request):
	cnt = 0
	plt = ""
	x = 0
	curr = os.getcwd()
	d = curr + "/downloadable"
	conf = get_config(d)
	message = ""
	df = readcsv(d, 'fullycleaned.csv')
	prevlines = get_data("lines counter", conf)
	save_to_config_func(prevlines - len(df),
						"lines counter after cleaning", conf)

	# I generated a form that has checkboxes depending on the correlation table
	if request.method == 'POST':
		form = TransformForm(request.POST)
		transform = request.POST.get('technique')
		tar = get_data('prediction', conf)

		X, y = split(df, tar)

		# Here we will be checking the type of our Regression (Binary or multi-class classification or regression)
		save_to_config_func(determine(y), "problem type", conf)

		if(transform == '1'):  # PCA
			save_to_config_func('Principle Component Analysis',
								'transformation technique', conf)
			final = pca(df, tar)
			# print(final)
			final.to_csv(curr + '/downloadable/transformed.csv', index=False)
			cnt = colcnt(final)
		elif(transform == '2'):
			save_to_config_func('Linear Discrimination Analysis',
								'transformation technique', conf)
			final = LDA(df, tar)
			final.to_csv(curr + '/downloadable/transformed.csv', index=False)
		else:
			save_to_config_func('Factor Analysis',
								'transformation technique', conf)
			final = FA(df, tar)
			final.to_csv(curr + '/downloadable/transformed.csv', index=False)

	return render(request, 'correlation.html', {'cnt': cnt, 'trans': transform})

# We'll be returning to the user the model, the accuracy, the config file and the cleaned and transformed csvs to download


def modelling(request):
	directory = os.getcwd()
	message = ""
	acc = 0
	pth = directory + "/downloadable/"
	df = readcsv(pth, 'transformed.csv')
	conf = get_config(pth)

	mod = get_data("preferred model", conf)
	probtype = get_data("problem type", conf)
	tar = get_data("prediction", conf)
	c = get_data("format", conf)
	# Use set instead of list to lower complexity O(1) instead of O(n)
	if mod in {"CNN", "ANN"}:
		if c in {"One CSV", "Multiple CSVs", "One Json", "Multiple Jsons"}:
			message = "There is no image folder for the Neural Network so another model will be selected"
			if probtype == "Classification":
				mod = "Logistic Regression"
			else:
				mod = "Linear Regression"

	elif mod in {"Linear Regression", "Logistic Regression"}:
		if c in {"Images with their CSV", "Images with their Json", "Images with their txt", "Images with their XML"}:
			message = "There is an image folder that shouldn't be there so another model will be selected"
			mod = "CNN"
		elif probtype == "Classification":
			mod = "Logistic Regression"
		else:
			mod = "Linear Regression"

	elif c in {"One CSV", "Multiple CSVs", "One Json", "Multiple Jsons"}:
		message = "We will be proceeding to training your regression/classification model"
		if probtype == "Classification":
			mod = "Logistic Regression"
		else:
			mod = "Linear Regression"
	else:
		message = "We will be proceeding to training your CNN model"
		mod = "CNN"
	if mod == "Linear Regression":
		X, y = split(df, tar)
		acc1 = train_LR(X, y)
		acc2 = train_GBR(X, y)
		if acc1 >= acc2:
			save_to_config_func("Linear Regression", "chosen model", conf)
			acc = acc1
			save_to_config_func(acc1, "accuracy", conf)
		else:
			save_to_config_func("Gradient Boosting Regression", "chosen model", conf)
			acc = acc2
			save_to_config_func(acc2, "accuracy", conf)
		conf = pth + conf
		cleaned = pth + "fullycleaned.csv"
		trans = pth + "transformed.csv"
	else:
		# Here will be out Logistic Regression
		print("LOGISTIC")
	#TODO : clean the forms file
	return render(request, 'modeltemp.html', {'message': message, 'mod': mod, 'acc': acc, 'conf': conf, 'cleaned': cleaned, 'trans': trans})