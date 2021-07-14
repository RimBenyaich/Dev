'''
Here will be our form in addition to the one that will be generated depending on the DF
for dropping features
'''
from django import forms

class HomeForm(forms.Form):
	project_name = forms.CharField(label = 'Project Name')
	url = forms.URLField(label='Google Drive URL')
	file_types = [(1,'One CSV file'),(2,'Multiple CSV files'),(3,'One Json file'),(4,'Multiple Json files'),(5,'Images with their CSV file'),(6,'Images with their Json file'),(7,'Images with their txt file'),(8,'Images with their XML file')]
	choice = forms.ChoiceField(label = 'Files Format', widget=forms.RadioSelect, choices=file_types)
	problem_types = [(1,"Regression"),(2,"Classification")]
	probtype = forms.ChoiceField(label='Type of Problem', choices=problem_types)
	models = [(1,"CNN"),(2,"ANN"),(3,"Linear Regression"),(4,"Logistic Regression"),(5,"Any")]
	preferred = forms.ChoiceField(label='Model preferred', choices=models)

class TransformForm(forms.Form):
	techniques = [(1,'Principle Component Analysis'),(2,'Linear Discriminent Analysis'),(3,'Factor Analysis')] #,(3,'Max'),(4,'Min')
	technique = forms.ChoiceField(
		label='Please indicate the Dimension Reduction technique desired', widget=forms.RadioSelect, choices=techniques)

class DropFeat(forms.Form):
	pass

class CheckForm(forms.Form):
	pass

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class DropFeat(forms.Form):
	age = forms.BooleanField(required = False, label="age - -0.2214",initial = False)
	sex = forms.BooleanField(required = False, label="sex - -0.2832",initial = False)
	cp = forms.BooleanField(required = False, label="cp - 0.4298",initial = False)
	trtbps = forms.BooleanField(required = False, label="trtbps - -0.1455",initial = False)
	chol = forms.BooleanField(required = False, label="chol - -0.0826",initial = False)
	fbs = forms.BooleanField(required = False, label="fbs - -0.0333",initial = False)
	restecg = forms.BooleanField(required = False, label="restecg - 0.1419",initial = False)
	thalachh = forms.BooleanField(required = False, label="thalachh - 0.4180",initial = False)
	exng = forms.BooleanField(required = False, label="exng - -0.4332",initial = False)
	oldpeak = forms.BooleanField(required = False, label="oldpeak - -0.4476",initial = False)
	slp = forms.BooleanField(required = False, label="slp - 0.3652",initial = False)
	caa = forms.BooleanField(required = False, label="caa - -0.3878",initial = False)
	thall = forms.BooleanField(required = False, label="thall - -0.3387",initial = False)

class DropFeat(forms.Form):
	age = forms.BooleanField(required = False, label="age - -0.2214",initial = False)
	sex = forms.BooleanField(required = False, label="sex - -0.2832",initial = False)
	cp = forms.BooleanField(required = False, label="cp - 0.4298",initial = False)
	trtbps = forms.BooleanField(required = False, label="trtbps - -0.1455",initial = False)
	chol = forms.BooleanField(required = False, label="chol - -0.0826",initial = False)
	fbs = forms.BooleanField(required = False, label="fbs - -0.0333",initial = False)
	restecg = forms.BooleanField(required = False, label="restecg - 0.1419",initial = False)
	thalachh = forms.BooleanField(required = False, label="thalachh - 0.4180",initial = False)
	exng = forms.BooleanField(required = False, label="exng - -0.4332",initial = False)
	oldpeak = forms.BooleanField(required = False, label="oldpeak - -0.4476",initial = False)
	slp = forms.BooleanField(required = False, label="slp - 0.3652",initial = False)
	caa = forms.BooleanField(required = False, label="caa - -0.3878",initial = False)
	thall = forms.BooleanField(required = False, label="thall - -0.3387",initial = False)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class DropFeat(forms.Form):
	age = forms.BooleanField(required = False, label="age - -0.2242",initial = False)
	sex = forms.BooleanField(required = False, label="sex - -0.2821",initial = False)
	cp = forms.BooleanField(required = False, label="cp - 0.4280",initial = False)
	trtbps = forms.BooleanField(required = False, label="trtbps - -0.1452",initial = False)
	chol = forms.BooleanField(required = False, label="chol - -0.0852",initial = False)
	fbs = forms.BooleanField(required = False, label="fbs - -0.0280",initial = False)
	restecg = forms.BooleanField(required = False, label="restecg - 0.1372",initial = False)
	thalachh = forms.BooleanField(required = False, label="thalachh - 0.4217",initial = False)
	exng = forms.BooleanField(required = False, label="exng - -0.4368",initial = False)
	oldpeak = forms.BooleanField(required = False, label="oldpeak - -0.4307",initial = False)
	slp = forms.BooleanField(required = False, label="slp - 0.3459",initial = False)
	caa = forms.BooleanField(required = False, label="caa - -0.3917",initial = False)
	thall = forms.BooleanField(required = False, label="thall - -0.3440",initial = False)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class DropFeat(forms.Form):
	age = forms.BooleanField(required = False, label="age - -0.2226",initial = False)
	sex = forms.BooleanField(required = False, label="sex - -0.2801",initial = False)
	cp = forms.BooleanField(required = False, label="cp - 0.4304",initial = False)
	trtbps = forms.BooleanField(required = False, label="trtbps - -0.1457",initial = False)
	chol = forms.BooleanField(required = False, label="chol - -0.0898",initial = False)
	fbs = forms.BooleanField(required = False, label="fbs - -0.0320",initial = False)
	restecg = forms.BooleanField(required = False, label="restecg - 0.1395",initial = False)
	thalachh = forms.BooleanField(required = False, label="thalachh - 0.4170",initial = False)
	exng = forms.BooleanField(required = False, label="exng - -0.4398",initial = False)
	oldpeak = forms.BooleanField(required = False, label="oldpeak - -0.4472",initial = False)
	slp = forms.BooleanField(required = False, label="slp - 0.3632",initial = False)
	caa = forms.BooleanField(required = False, label="caa - -0.3865",initial = False)
	thall = forms.BooleanField(required = False, label="thall - -0.3377",initial = False)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class DropFeat(forms.Form):
	age = forms.BooleanField(required = False, label="age - -0.2235",initial = False)
	sex = forms.BooleanField(required = False, label="sex - -0.2828",initial = False)
	cp = forms.BooleanField(required = False, label="cp - 0.4346",initial = False)
	trtbps = forms.BooleanField(required = False, label="trtbps - -0.1440",initial = False)
	chol = forms.BooleanField(required = False, label="chol - -0.0893",initial = False)
	fbs = forms.BooleanField(required = False, label="fbs - -0.0308",initial = False)
	restecg = forms.BooleanField(required = False, label="restecg - 0.1371",initial = False)
	thalachh = forms.BooleanField(required = False, label="thalachh - 0.4148",initial = False)
	exng = forms.BooleanField(required = False, label="exng - -0.4386",initial = False)
	oldpeak = forms.BooleanField(required = False, label="oldpeak - -0.4473",initial = False)
	slp = forms.BooleanField(required = False, label="slp - 0.3613",initial = False)
	caa = forms.BooleanField(required = False, label="caa - -0.3851",initial = False)
	thall = forms.BooleanField(required = False, label="thall - -0.3367",initial = False)

class CheckForm(forms.Form):
	CHOICES1 = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	age = forms.ChoiceField(label = 'age has 2 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	sex = forms.ChoiceField(label = 'sex has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	cp = forms.ChoiceField(label = 'cp has 4 missing values', widget=forms.RadioSelect, choices=CHOICES1)
	trtbps = forms.ChoiceField(label = 'trtbps has 3 missing values', widget=forms.RadioSelect, choices=CHOICES1)

class DropFeat(forms.Form):
	age = forms.BooleanField(required = False, label="age - -0.2248",initial = False)
	sex = forms.BooleanField(required = False, label="sex - -0.2828",initial = False)
	cp = forms.BooleanField(required = False, label="cp - 0.4223",initial = False)
	trtbps = forms.BooleanField(required = False, label="trtbps - -0.1453",initial = False)
	chol = forms.BooleanField(required = False, label="chol - -0.0849",initial = False)
	fbs = forms.BooleanField(required = False, label="fbs - -0.0345",initial = False)
	restecg = forms.BooleanField(required = False, label="restecg - 0.1384",initial = False)
	thalachh = forms.BooleanField(required = False, label="thalachh - 0.4198",initial = False)
	exng = forms.BooleanField(required = False, label="exng - -0.4344",initial = False)
	oldpeak = forms.BooleanField(required = False, label="oldpeak - -0.4459",initial = False)
	slp = forms.BooleanField(required = False, label="slp - 0.3671",initial = False)
	caa = forms.BooleanField(required = False, label="caa - -0.3891",initial = False)
	thall = forms.BooleanField(required = False, label="thall - -0.3396",initial = False)
