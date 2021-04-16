from django.shortcuts import render
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
from .clean import handlemiss
import os
# https://drive.google.com/drive/u/0/folders/1SfNihWNYJQPsniZ-yjQN6lgl1sUYw6RL

conf = ''
img_dir = '/images'
path = ''
# Create your views here.
def UI(request):
	conf = 'config_'
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
			# return redirect('/download', {'conf' : conf})
	else:
		form = HomeForm()
	return render(request, 'home.html', {'form': form})

def checking(request):
	directory = os.getcwd();
	message = ""

	conf = get_config(directory)
	message = checks(conf)
	# print(message)
	if(message != "check"):
		print(message)
		return render(request, 'notchecked.html', {'message': message})
	categs = get_columns(conf)
	num = missingcount(conf)
	dic = check_missing(conf)
	# print(num)
	if(num == 0):
		return render(request, 'checked.html', {'num': num, 'categs': categs})
	else:
		form = CheckForm()
		return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form, 'categs': categs})

def clean(request):
	curr = os.getcwd()
	dic = [""]
	num = 0
	if request.method == 'POST':
		form = CheckForm(request.POST)
		if form.is_valid():
			missing = request.POST.get('missing')
			indtar = request.POST.get('indtar')
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
			indtar = int(indtar)
			conf = get_config(curr)
			dic = check_missing(conf)
			directory = './' + get_data("project_name", conf)
			num = get_data("lines counter", conf)
			
			save_to_config_func(way, 'missing', conf)
			save_to_config_func(indtar, 'target', conf)
			save_to_config_func(nametar, 'prediction', conf)
			df = handlemiss(way, directory)
			newnum = num - len(df)
			save_to_config_func(len(df), "lines counter after cleaning", conf)
			return render(request, 'clean.html', {'conf': conf, 'num': newnum})
	else:
		form = CheckForm()
	# checking(path, conf)
	return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form})

def correlation(request):
	render(request, 'corr.html', {})