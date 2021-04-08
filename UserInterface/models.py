from django.db import models

# Create your models here.
class Configuration(models.Model):
	config_name = models.CharField()
	project_name = models.CharField()
	url = models.URLField()
	choice = models.DecimalField()
	preferred = models.CharField()

	class Meta:
		abstract = True