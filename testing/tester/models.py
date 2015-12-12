from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tester(models.Model):
	id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
	hash = models.CharField(max_length=30)