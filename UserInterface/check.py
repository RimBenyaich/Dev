import os
from os import path
from pathlib import Path
from .files import get_conf_categ

# checks types of given files and whether they match the choice given by the user

def checking(directory, conf):
	choice = get_conf_categ('choice', conf)

	print(type(choice))

def check_ext(directory, ext):
	for filename in os.listdir(directory):
		# print(filename)
		p = Path(directory)
		q = p / filename
		if not filename.endswith(ext):
			if not q.is_dir():
				print('There are files with undeclared extension')
				return False
	return True