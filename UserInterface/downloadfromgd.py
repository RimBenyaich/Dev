from bs4 import BeautifulSoup as bs
import requests
from .googledrive import GoogleDriveDownloader as gdd

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