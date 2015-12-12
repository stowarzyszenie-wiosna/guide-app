from __future__ import unicode_literals
from tester.models import *

from django.db import models
	
class Step(models.Model):
	scenario = models.ForeignKey(Tester,related_name='steps')
	content =  models.CharField(max_length=1024)
	