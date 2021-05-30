'''
Here will be our form in addition to the one that will be generated depending on the DF
for dropping features
'''
from django import forms

class HomeForm(forms.Form):
	project_name = forms.CharField(label = 'Project Name')
	url = forms.URLField(label='Google Drive URL')
	CHOICES = [(1,'One CSV file'),(2,'Multiple CSV files'),(3,'One Json file'),(4,'Multiple Json files'),(5,'Images with their CSV file'),(6,'Images with their Json file'),(7,'Images with their txt file'),(8,'Images with their XML file')]
	choice = forms.ChoiceField(label = 'Files Format', widget=forms.RadioSelect, choices=CHOICES)
	CHOICES = [(1,"CNN"),(2,"ANN"),(3,"Linear Regression"),(4,"Logistic Regression"),(5,"Any")]
	preferred = forms.ChoiceField(label= 'Model preferred', choices=CHOICES)

class TransformForm(forms.Form):
	CHOICES = [(1,'Principle Component Analysis'),(2,'Linear Discriminent Analysis'),(3,'Factor Analysis')] #,(3,'Max'),(4,'Min')

	technique = forms.ChoiceField(label = 'Please indicate the Dimension Reduction technique desired', widget=forms.RadioSelect, choices=CHOICES)

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


