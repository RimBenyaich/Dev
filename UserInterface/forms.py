from django import forms

class HomeForm(forms.Form):
	project_name = forms.CharField(label = 'Project Name')
	url = forms.URLField(label='Google Drive URL')
	CHOICES = [(1,'One CSV file'),(2,'Multiple CSV files'),(3,'One Json file'),(4,'Multiple Json files'),(5,'Images with their CSV file'),(6,'Images with their Json file'),(7,'Images with their txt file'),(8,'Images with their XML file')]
	choice = forms.ChoiceField(label = 'Files Format', widget=forms.RadioSelect, choices=CHOICES)
	CHOICES = [(1,"CNN"),(2,"ANN"),(3,"Linear Regression"),(4,"Logistic Regression"),(5,"Any")]
	preferred = forms.ChoiceField(label= 'Model preferred', choices=CHOICES)

class CheckForm(forms.Form):
	# def __init__(self,*args,**kwargs):
	# 	self.categs = kwargs.pop('categs')
	# 	self.fields['dropcol'].initial = categs
	# 	super(CheckForm, self).__init__(*args,**kwargs)

	CHOICES = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	missing = forms.ChoiceField(label = 'Please indicate how you want to handle missing values', widget=forms.RadioSelect, choices=CHOICES)
	nametar = forms.CharField(label = 'Please indicate the name of the prediction')
	# dropcol = forms.MultipleChoiceField(required = False, label = 'Please select the column(s) you want to drop')

class DropFeat(forms.Form):
	ids = forms.BooleanField(required = False, label = "-0.0169")
	bedrooms = forms.BooleanField(required = False, label = "0.3083")
	bathrooms = forms.BooleanField(required = False, label = "0.5252")
	sqft_living = forms.BooleanField(required = False, label = "0.7021")
	sqft_lot = forms.BooleanField(required = False, label = "0.0897")
	floors = forms.BooleanField(required = False, label = "0.2568")
	waterfront = forms.BooleanField(required = False, label = "0.2664")
	view = forms.BooleanField(required = False, label = "0.3974")
	condition = forms.BooleanField(required = False, label = "0.0364")
	grade = forms.BooleanField(required = False, label = "0.6674")
	sqft_above = forms.BooleanField(required = False, label = "0.6056")
	sqft_basement = forms.BooleanField(required = False, label = "0.3238")
	yr_built = forms.BooleanField(required = False, label = "0.0539")
	yr_renovated = forms.BooleanField(required = False, label = "0.1264")
	zipcode = forms.BooleanField(required = False, label = "-0.0533")
	lat = forms.BooleanField(required = False, label = "0.3070")
	longi = forms.BooleanField(required = False, label = "0.0216")
	sqft_living15 = forms.BooleanField(required = False, label = "0.5854")
	sqft_lot15 = forms.BooleanField(required = False, label = "0.0824")

class DropFeat(forms.Form):
	ids = forms.BooleanField(required = False, label = "-0.0169")
	bedrooms = forms.BooleanField(required = False, label = "0.3083")
	bathrooms = forms.BooleanField(required = False, label = "0.5252")
	sqft_living = forms.BooleanField(required = False, label = "0.7021")
	sqft_lot = forms.BooleanField(required = False, label = "0.0897")
	floors = forms.BooleanField(required = False, label = "0.2568")
	waterfront = forms.BooleanField(required = False, label = "0.2664")
	view = forms.BooleanField(required = False, label = "0.3974")
	condition = forms.BooleanField(required = False, label = "0.0364")
	grade = forms.BooleanField(required = False, label = "0.6674")
	sqft_above = forms.BooleanField(required = False, label = "0.6056")
	sqft_basement = forms.BooleanField(required = False, label = "0.3238")
	yr_built = forms.BooleanField(required = False, label = "0.0539")
	yr_renovated = forms.BooleanField(required = False, label = "0.1264")
	zipcode = forms.BooleanField(required = False, label = "-0.0533")
	lat = forms.BooleanField(required = False, label = "0.3070")
	longi = forms.BooleanField(required = False, label = "0.0216")
	sqft_living15 = forms.BooleanField(required = False, label = "0.5854")
	sqft_lot15 = forms.BooleanField(required = False, label = "0.0824")
