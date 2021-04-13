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
from .check import checks
from .check import check_ext
from .check import check_missing
from .check import missingcount
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

def clean(request):
	if request.method == 'POST':
		form = CheckForm(request.POST)
		if form.is_valid():
			missing = request.POST.get('missing')
			indtar = request.POST.get('indtar')
			nametar = request.POST.get('nametar')
	else:
		form = CheckForm()
	return render(request, 'clean.html', {'conf': conf})
	# checking(path, conf)

	return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form})

def checking(request):
	directory = os.getcwd();
	message = ""

	conf = get_config(directory)
	message = checks(conf)
	# print(message)
	if(message != "check"):
		print(message)
		return render(request, 'notchecked.html', {'message': message})
	num = missingcount(conf)
	dic = check_missing(conf)
	print(num)
	if(num == 0):
		return render(request, 'checked.html', {'num': num})
	else:
		form = CheckForm()
		return render(request, 'checked.html', {'num': num, 'dic': dic, 'form': form})
