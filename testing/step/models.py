from __future__ import unicode_literals

from django.db import models
	
class Step(models.Model):
	id = models.AutoField(primary_key=True)
	scenario = models.ForeignKey(Tester,related_name='steps')
	content =  models.CharField(max_length=1024)
	