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