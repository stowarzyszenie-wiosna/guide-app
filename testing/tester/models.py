from __future__ import unicode_literals
from django.db import models


class Tester(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    hash = models.CharField(max_length=64)
