from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from .forms import HomeForm, TransformForm
from .downloadfromgd import recurs_folders
from .files import renaming
from .files import rename_conf
from .files import init_conf
from .files import save_to_config_form
from .files import save_to_config_func
from .files import get_config
from .files import get_data
from .check import checks
from .check import check_ext
from .check import check_missing
from .check import missingcount
from .datafr import dropcols, get_columns
from .datafr import readcsv
from .clean import handlemiss
from .modelrep import get_model_repr
from .Transform import split
from .Transform import corr
from .Transform import pca
from .Transform import LDA
from .Transform import FA
from .files import delete
from .gen_mod_py import generate
from .model import train_GBR
from .model import train_LR
from .genform import generateform
from .genform import genere
from .datafr import getcols
from .datafr import getdt
from .datafr import colcnt
from .datafr import getdt
from .genform import gencleanform
from .files import cleanfiles
import numpy as np
import pandas as pd
import os
# from .models import DFModel
# https://drive.google.com/drive/u/0/folders/1SfNihWNYJQPsniZ-yjQN6lgl1sUYw6RL

conf = ''
img_dir = '/images'
path = ''

# Here will be our home page
def UI(request):
	conf = 'config_'
	mod = ''
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
			new_conf = direct + conf
			conf = rename_conf(direct, conf, project_name)
			cnt = recurs_folders(new_r, cnt, path + '/')
			renaming(path, '.csv')
			form.cleaned_data
			init_conf(conf)
			save_to_config_form(request, form, conf)
			return render(request, 'download.html', { 'conf': conf})
	else:
		form = HomeForm()
	return render(request, 'home.html', {'form': form})

#Here, we will be checking the syntax and format of the file and check for any missing values
def checking(request):
	directory = os.getcwd()
	d = directory + "/downloadable"
	strcnt = 0
	message = ""
	dt = {}
	conf = get_config(d)
	message = checks(conf)
	
	if(message != "check"):
		delete(directory, conf)
		return render(request, 'notchecked.html', {'message': message})
	dire = './' + get_data("project_name", conf)
	
	df = readcsv(dire, 'none')
	categs = get_columns(conf)
	num = missingcount(conf)
	dic = check_missing(conf)
	for key, value in dic.items():
		if value > 0:
			dt[key] = str(df.dtypes[key])
	
	save_to_config_func(dt, 'missing values datatype', conf)
	out = gencleanform(dic, dt)
	genere(out)
	cnt = len(categs)
	if(num == 0):
		form = CheckForm()
		return render(request, 'checked.html', {'num': num, 'categs': categs, 'form': form})
	else:
		form = CheckForm()
		return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form, 'categs': categs, 'cnt': cnt, 'dt': dt})

#Here, we will be handling the missing values
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
		if form.is_valid():
			# Here will be the for loop that will regroup our handling for each missing value
			dic = get_data("missing values datatype",conf)
			# print(dic)
			# print(len(dic))
			for key in dic:
				if(dic[key] == 'float64' or dic[key] == 'int64'):
					x = int(request.POST.get(key))
					if(x == 1):
						nums[key] = "Drop"
					elif x == 2:
						nums[key] = "Mean"
					elif x == 3:
						nums[key] = "Max"
					else:
						nums[key] = "Min"
				else:
					categs[key] = int(request.POST.get(key))
					if(x == 1):
						nums[key] = "Drop"
					elif x == 2:
						nums[key] = "Mode"
			nametar = request.POST.get('nametar')
			save_to_config_func(nums, 'handlemissingnums', conf)
			save_to_config_func(categs, 'handlemissingcategs', conf)
			directory = './' + get_data("project_name", conf)
			num = get_data("lines counter", conf)
			save_to_config_func(nametar, 'prediction', conf)
			save_to_config_func(len(dic), 'handlecolcnt', conf)
			df = handlemiss(nums, categs, directory)
			x = len(df[nametar].unique())
			newnum = len(dic)
			save_to_config_func(len(df), "lines counter after cleaning", conf)
			#here I'll need to generate the model for my df and save it there
			# X, y = split(df, nametar)
			# print(curr)
			#Here we will be transforming our categorical values
			obj_df = df.select_dtypes(include=['object']).copy()
			for col in obj_df:
				df[col] = df[col].astype('category')
				pd.get_dummies(df, columns=[col])

			#TODO separate the normal categories from datetime formats
			for col in df:
				if col == "date":
					x = df[col].str.len()
					if x[1] == 15:
						df[col] = df[col].str.slice(0, 8)
						df[col] = df[col].astype(int)
			correl = corr(df, nametar)
			# print(correl)
			newf = generateform(correl, nametar)
			genere(newf)
			df.to_csv(curr + '/downloadable/cleaned.csv', index = False)
			# generate(get_model_repr(df))
			form = DropFeat()
			return render(request, 'clean.html', {'form': form,'conf': conf, 'num': newnum, 'corr': correl, 'target': nametar})
			# return HttpResponse(df.to_html())
	else:
		form = CheckForm()
	# checking(path, conf)
	return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form})

'''
In this section, we will be continuing the cleaning (dropping features selected by the user)
'''
def cleancontinued(request):
	cat = []
	curr = os.getcwd()
	d = curr + "/downloadable/"
	conf = get_config(d)
	message = ""
	items = []
	categs = []
	cnt = 0
	df = readcsv(d, 'none')

	#I generated a form that has checkboxes depending on the correlation table
	if request.method == 'POST' or None:
		categs = getcols(df)
		form = DropFeat(request.POST or None)
		for col in categs:
			if request.POST.get(col) == 'on':
				items.append(col)
				cnt += 1
		# print
		if cnt == 0:
			df.to_csv(curr + '/downloadable/fullycleaned.csv', index = False)
			if os.path.exists(curr + "/downloadable/cleaned.csv"):
				os.remove(curr + "/downloadable/cleaned.csv") 
			message = "No columns will be dropped"
			
			form = TransformForm()
			return render(request, 'cleancontinued.html', {'form': form, 'message': message, 'cnt': cnt})
		else:
			#We make changes on df aka drop the selected columns and return the new df
			save_to_config_func(items, 'colstodrop', conf)
			newdf = dropcols(items, df)
			#Haven't decided yet whether we should delete cleaned.csv and keep fullycleaned or keep them both
			newdf.to_csv(curr + '/downloadable/fullycleaned.csv', index = False)

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
	month, year, day = "", "", ""
	curr = os.getcwd()
	d = curr + "/downloadable"
	conf = get_config(d)
	message = ""
	df = readcsv(d, 'fullycleaned.csv')
	# print(df)

	#I generated a form that has checkboxes depending on the correlation table
	# print(df)
	if request.method == 'POST' :
		form = TransformForm(request.POST)
		transform = request.POST.get('technique')

		# print(transform)
		
		# #Here we will be transforming our categorical values
		# obj_df = df.select_dtypes(include=['object']).copy()
		# for col in obj_df:
		# 	df[col] = df[col].astype('category')
		# 	pd.get_dummies(df, columns=[col])

		# #TODO separate the normal categories from datetime formats
		# for col in df:
		# 	if col == "date":
		# 		x = df[col].str.len()
		# 		# print(x[2])
		# 		if x[1] == 15:
		# 			df[col] = df[col].str.slice(0, 8)
		# 			df[col] = df[col].astype(int)
		
		if(transform == '1'): #PCA
			tar = get_data('prediction',conf)
			final = pca(df, tar)
			# print(final)
			final.to_csv(curr + '/downloadable/transformed.csv', index = False)
			cnt = colcnt(final)
		elif(transform == '2'):
			final = LDA(df, tar)
			final.to_csv(curr + '/downloadable/transformed.csv', index = False)
		else:
			final = FA(df, tar)
			final.to_csv(curr + '/downloadable/transformed.csv', index = False)
			# print("hjere")
		#2 is LDA and 3 is FA
		
	return render(request, 'correlation.html', {'cnt': cnt})

# We'll be returning to the user the model, the accuracy, the config file and the cleaned
# and transformed csvs to download

def modelling(request):
	directory = os.getcwd();
	message = ""
	chosen = ""
	cc = 0
	pth = directory + "/downloadable/" 
	df = readcsv(pth, 'transformed.csv')
	conf = get_config(pth)

	mod = get_data("preferred", conf)
	tar = get_data("prediction", conf)
	c = get_data("choice", conf)

	if(mod == 1 or mod == 2):
		if(c == 1 or c == 2 or c == 3 or c == 4):
			message = "There is no image folder for the Neural Network so another model will be selected"
			mod = 3
	elif(mod == 3 or mod == 4):
		if(c== 5 or c == 6 or c == 7 or c == 8):
				message = "There is an image folder that shouldn't be there so another model will be selected"
				mod = 1
	else:
		if(c == 1 or c == 2 or c == 3 or c == 4):
			message = "We will be proceeding to training your regression/classification model"
			mod = 3
		else:
			mod = 1
	if mod == 3:
		X, y = split(df, tar)
		acc1 = train_LR(X, y)
		acc2 = train_GBR(X, y)
		if acc1 >= acc2:
			chosen = "Logistic regression"
			cc = acc1
		else:
			chosen = "Gradient Boosting Regression"
			cc = acc2

	return render(request, 'model.html', {'message': message, 'mod': mod, 'chosen': chosen, 'acc': cc})

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	bathrooms = forms.ChoiceField(label = 'bathrooms has 1 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	view = forms.ChoiceField(label = 'view has 1 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sqft_above = forms.ChoiceField(label = 'sqft_above has 1 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	yr_renovated = forms.ChoiceField(label = 'yr_renovated has 1 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	zipcode = forms.ChoiceField(label = 'zipcode has 1 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	nametar = forms.CharField(label = 'Please indicate the name of the prediction')


class DropFeat(forms.Form):
	ids = forms.BooleanField(required = False, label="ids - -0.0169",initial = False)
	date = forms.BooleanField(required = False, label="date - 0.0030",initial = False)
	bedrooms = forms.BooleanField(required = False, label="bedrooms - 0.3083",initial = False)
	bathrooms = forms.BooleanField(required = False, label="bathrooms - 0.5252",initial = False)
	sqft_living = forms.BooleanField(required = False, label="sqft_living - 0.7021",initial = False)
	sqft_lot = forms.BooleanField(required = False, label="sqft_lot - 0.0897",initial = False)
	floors = forms.BooleanField(required = False, label="floors - 0.2568",initial = False)
	waterfront = forms.BooleanField(required = False, label="waterfront - 0.2664",initial = False)
	view = forms.BooleanField(required = False, label="view - 0.3974",initial = False)
	condition = forms.BooleanField(required = False, label="condition - 0.0364",initial = False)
	grade = forms.BooleanField(required = False, label="grade - 0.6674",initial = False)
	sqft_above = forms.BooleanField(required = False, label="sqft_above - 0.6056",initial = False)
	sqft_basement = forms.BooleanField(required = False, label="sqft_basement - 0.3238",initial = False)
	yr_built = forms.BooleanField(required = False, label="yr_built - 0.0539",initial = False)
	yr_renovated = forms.BooleanField(required = False, label="yr_renovated - 0.1264",initial = False)
	zipcode = forms.BooleanField(required = False, label="zipcode - -0.0533",initial = False)
	lat = forms.BooleanField(required = False, label="lat - 0.3070",initial = False)
	longi = forms.BooleanField(required = False, label="longi - 0.0216",initial = False)
	sqft_living15 = forms.BooleanField(required = False, label="sqft_living15 - 0.5854",initial = False)
	sqft_lot15 = forms.BooleanField(required = False, label="sqft_lot15 - 0.0824",initial = False)


#TODO check the number of targets to know whether its a binary classification or predictions