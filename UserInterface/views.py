from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm
from .downloadfromgd import recurs_folders
from .files import renaming
from .files import rename_conf
from .files import init_conf
from .files import save_to_config_form
from .files import save_to_config_func
from .check import checking
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
			# os.mkdir(path)
			# path = './data'
			cnt = recurs_folders(new_r, cnt, path + '/')
			renaming(path, '.csv')
			form.cleaned_data
			init_conf(conf)
			save_to_config_form(request, form, conf)

			return render(request, 'download.html', {'form':form, 'conf': conf})
	else:
		form = HomeForm()
	return render(request, 'home.html', {'form':form})

def check(request):
	checking(path, conf)

	return render(request, 'check.html', {})

def download(request):
	return render(request, 'download.html', {})
