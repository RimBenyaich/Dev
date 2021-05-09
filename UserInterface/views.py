from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm
from .forms import CheckForm
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
from .datafr import get_columns
from .datafr import readcsv
from .clean import handlemiss
from .modelrep import get_model_repr
from .pca import split
from .pca import corr
from .files import delete
from .gen_mod_py import generate
from .model import train_GBR
from .model import train_LR
from .genform import generateform
from .genform import genere
import os
# from .models import DFModel
# https://drive.google.com/drive/u/0/folders/1SfNihWNYJQPsniZ-yjQN6lgl1sUYw6RL

conf = ''
img_dir = '/images'
path = ''
# Create your views here.
def UI(request):
	conf = 'config_'
	mod = ''
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():
			project_name = request.POST.get('project_name')
			url = request.POST.get('url')
			new_r = url.split('/')[-1]
			cnt = 0
			path = './' + project_name
			new_conf = path + conf
			conf = rename_conf(path, conf, project_name)
			cnt = recurs_folders(new_r, cnt, path + '/')
			renaming(path, '.csv')
			form.cleaned_data
			init_conf(conf)
			save_to_config_form(request, form, conf)
			return render(request, 'download.html', { 'conf': conf})
	else:
		form = HomeForm()
	return render(request, 'home.html', {'form': form})

def checking(request):
	directory = os.getcwd()
	strcnt = 0
	message = ""
	dt = {}

	conf = get_config(directory)
	message = checks(conf)
	# print(message)
	if(message != "check"):
		print(message)
		delete(directory, conf)
		return render(request, 'notchecked.html', {'message': message})
	dire = './' + get_data("project_name", conf)
	df = readcsv(dire)
	categs = get_columns(conf)
	num = missingcount(conf)
	dic = check_missing(conf)
	for key, value in dic.items():
		if value > 0:
			dt[key] = df.dtypes[key]
			# print(key)
			# print(dt[key])
			if dt[key] == "object":
				strcnt += 1
	cnt = len(categs)
	if(num == 0):
		form = CheckForm()
		return render(request, 'checked.html', {'num': num, 'categs': categs})
	else:
		form = CheckForm()
		return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form, 'categs': categs, 'cnt': cnt, 'dt': dt})
		
def clean(request):
	curr = os.getcwd()
	dic = [""]
	num = 0
	if request.method == 'POST':
		form = CheckForm(request.POST)
		if form.is_valid():
			missing = request.POST.get('missing')
			nametar = request.POST.get('nametar')
			missing = int(missing)
			if missing == 1:
				way = "drop"
			elif missing == 2:
				way = "mean"
			elif missing == 3:
				way = "max"
			else:
				way = "min"
			conf = get_config(curr)
			dic = check_missing(conf)
			directory = './' + get_data("project_name", conf)
			num = get_data("lines counter", conf)
			
			save_to_config_func(way, 'missing', conf)
			save_to_config_func(nametar, 'prediction', conf)
			df = handlemiss(way, directory)
			newnum = num - len(df)
			save_to_config_func(len(df), "lines counter after cleaning", conf)
			#here I'll need to generate the model for my df and save it there
			# X, y = split(df, nametar)
			correl = corr(df, nametar)
			newf = generateform(correl, nametar)
			genere(newf)
			df.to_csv('cleaned.csv', index = False)
			# generate(get_model_repr(df))
			return render(request, 'clean.html', {'conf': conf, 'num': newnum, 'corr': correl, 'target': nametar})
			# return HttpResponse(df.to_html())
	else:
		form = CheckForm()
	# checking(path, conf)
	return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form, 'cnt': cnt})

def correlation(request):
	message = ""
	items = []
	curr = os.getcwd()
	df = readcsv(curr)
	# print(df)
	'''
	I need to generate a form that has checkboxes depending on the correlation table
	'''
	if request.method == 'POST':
		form = DropFeat(request.POST)
		message = "Items are about to be dropped"
		# items = request.POST.getlist('dropitems')
		# items = request.POST.get('dropitems')
		# print(items)
		#We make changes on df aka drop the selected columns and return the new df
		return render(request, 'correlation.html', {"items": items, "form": form})
		# for i in items:
		# 	print(i)
	else:
		form = DropFeat()
		message = "No feature was dropped"
		print(message)
	df = request.GET.get('df', '')
	# else return old df
	return render(request, 'correlation.html', {"form": form})

def modelling(request):
	directory = os.getcwd();
	message = ""
	X, y = 0

	conf = get_config(directory)

	mod = get_data("preferred", conf)
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
			mod = 3
		else:
			mod = 1
	if mod == 3:
		acc1 = train_LR(X, y)
		acc2 = train_GBR(X, y)


	return render(request, 'model.html', {'message': message})