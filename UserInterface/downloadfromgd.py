from bs4 import BeautifulSoup as bs
import requests
from .googledrive import GoogleDriveDownloader as gdd
from zipfile import ZipFile
import os

# url = "https://drive.google.com/drive/u/0/folders/1SfNihWNYJQPsniZ-yjQN6lgl1sUYw6RL"
# url = "https://drive.google.com/drive/u/0/folders/17zEX-kdFrP5kKX8yVK9auJfIrMopYyvw"
# url = "https://drive.google.com/drive/u/0/folders/1e1X_wgLnGMB1cwrEu4xrzQ9fuv0rUJpG"
# url = "https://drive.google.com/drive/u/0/folders/1m3iA_eTTYnbSgKyNrjiVqigUcZQF7FjH"
# url = "https://drive.google.com/drive/u/0/folders/1p2_I3LIGGFxX5a6gbAzrvMNyDm7eaMTG"

# x = 0

def recurs_folders(id, cnt,path):
	url = "https://drive.google.com/drive/u/0/folders/" + id
	req = requests.get(url)
	soup = bs(req.content, 'html.parser')
	body = soup.findAll('div', {'data-target':'doc'})
	ids = []
	names = []
	for d in body:
		ID = d.get('data-id')
		new_htm = d.find('div', {'data-tooltip' : True})
		EXT = new_htm.get('data-tooltip')
		if ID is not None:
			ids.append(ID)
		if EXT.endswith('.jpeg') or EXT.endswith('.jpg') or EXT.endswith('.png'):
			names.append(EXT)
			extra = 'images/'
			gdd.download_file_from_google_drive(ID, path + extra + names[cnt])
			cnt = cnt + 1
		elif EXT.endswith('csv') or EXT.endswith('json') or EXT.endswith('zip'):
			names.append(EXT)
			gdd.download_file_from_google_drive(ID, path + names[cnt])
			cnt = cnt + 1
			
		else:
			recurs_folders(ID, cnt, path)

# recurs_folders(ID, cnt, path)
# print(x)

def unz(directory):
	for file in os.listdir(directory):
		if(file.endswith('.zip')):
			# print(file)
			f = directory + "/" +  file
			with ZipFile(f, 'r') as zipObj:
				# Get a list of all archived file names from the zip
				listOfNames = zipObj.namelist()
				# Iterate over the file names
				for fileName in listOfNames:
					# Check filename endswith csv
					if fileName.endswith('.jpeg'):
						zipObj.extract(fileName,directory + '/images')
					else:
						zipObj.extract(fileName, directory)
			os.remove(directory + '/' + file)

# directory = './answer'

# for file in os.listdir(directory):
# 	if(file.endswith('.zip')):
# 		# print(file)
# 		f = directory + "/" +  file
# 		with ZipFile(f, 'r') as zipObj:
# 		   	# Get a list of all archived file names from the zip
# 		   	listOfNames = zipObj.namelist()
# 		   	# Iterate over the file names
# 		   	for fileName in listOfNames:
# 		   		# Check filename endswith csv
# 		   		if fileName.endswith('.csv'):
# 		   			zipObj.extract(fileName, directory)
# 		   		elif fileName.endswith('.jpeg'):
# 		   			zipObj.extract(fileName,directory + '/images')
# 		os.remove(directory + '/' + file)
# directory = directory + "/images"
# for filename in os.listdir(directory):
# 	if(filename.endswith('.jpeg')):
# 		#move file to images folder
# 		print('img')
# 	else:
# 		continue

# recurs_folders(ID, cnt,cntzip,cntimg,cntcsv)

# req = requests.get(url)

# soup = bs(req.content, 'html.parser')
# body = soup.findAll('div', {'data-target':'doc'})

# ids = []
# names = []
# ext = []
# cntimg = 1
# cntzip = 1
# cntcsv = 1
# cntfld = 1
# for d in body:
#      ID = d.get('data-id')
#      # recurs_folders(ID)
#      new_htm = d.find('div', {'data-tooltip' : True} )
#      EXT = new_htm.get('data-tooltip')
#      if ID is not None:
#          ids.append(ID)

#      #print(ID)
#      #print(new_htm)
#      #print(EXT)
#      if EXT.endswith(".zip"):
#      	ext.append(".zip")
#      	names.append('compress' + str(cntzip))
#      	cntzip = cntzip + 1

#      elif EXT.endswith('.jpeg') or EXT.endswith('.jpg') or EXT.endswith('.png'):
#      	ext.append('.jpeg')
#      	names.append('image' + str(cntimg))
#      	cntimg = cntimg + 1
#      elif EXT.endswith('csv'):
#      	ext.append('.csv')
#      	names.append('table' + str(cntcsv))
#      	cntcsv = cntcsv + 1
#      else:
#      	ext.append('')
#      	names.append('folder' + str(cntfld))
#      	cntfld = cntfld + 1

# # path = './answer/'
# # cnt = 0
# # for id in ids:
# # 	print(path + names[cnt] + ext[cnt])
# # # 	gdd.download_file_from_google_drive(id, path + names[cnt] + ext[cnt])
# #  	cnt = cnt + 1

# # print(body)