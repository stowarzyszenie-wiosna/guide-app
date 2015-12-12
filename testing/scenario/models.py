from django.db import models
from scenario.models import *


class Scenario(models.Model):
    name = models.CharField(max_length=100)
    site_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class Step(models.Model):
	scenario = models.ForeignKey(Scenario, related_name='steps')
	content =  models.CharField(max_length=1024)
