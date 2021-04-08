from django import forms

class HomeForm(forms.Form):
	project_name = forms.CharField(label = 'Project Name')
	url = forms.URLField(label='Google Drive URL')
	CHOICES = [(1,'One CSV file'),(2,'Multiple CSV files'),(3,'One Json file'),(4,'Multiple Json files'),(5,'Images with their CSV file'),(6,'Images with their Json file'),(7,'Images with their txt file'),(8,'Images with their XML file')]
	choice = forms.ChoiceField(label = 'Files Format', widget=forms.RadioSelect, choices=CHOICES)
	CHOICES = [(1,"CNN"),(2,"ANN"),(3,"Linear Regression"),(4,"Logistic Regression"),(5,"Any")]
	preferred = forms.ChoiceField(label= 'Model preferred', choices=CHOICES)

class CheckForm(forms.Form):
	CHOICES = [(1,'Drop'),(2,'Mean'),(3,'Max'),(4,'Min')]
	missing = forms.ChoiceField(label = 'Please indicate how you want to handle missing values', widget=forms.RadioSelect, choices=CHOICES)
	indtar = forms.DecimalField(label = 'Please indicate the index of the prediction')
	nametar = forms.CharField(label = 'Please indicate the name of the prediction')
'''
<input type="radio" id="mean" name="missing" value="mean">
		<label for="male">Mean</label><br>
		<input type="radio" id="max" name="missing" value="max">
		<label for="female">Max</label><br>
		<input type="radio" id="min" name="missing" value="min">
		<label for="other">Min</label><br>
		<input type="radio" id="drop" name="missing" value="drop">
		<label for="other">Drop</label>
	<br><br>
	<div> Please enter the index of the Target </div>
	<br>
	<input type = 'text' class='indtar'/>
	<br>
	<br>
	<div> Please enter the name of the Target </div>
	<br>
	<input type = 'text' class='target'/>
	<br>
	<br>

'''