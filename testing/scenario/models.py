from django.db import models
from scenario.models import *

STEP_TYPES = (
    (1, 'INFO'),
    (2, 'YES_OR_NO'),
    (3, 'ACTION'),
)


class Scenario(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='steps')
    site_url = models.URLField(max_length=200)


class Step(models.Model):
    group = models.ForeignKey(Group, related_name='steps')
    position = models.PositiveIntegerField()
    type = models.IntegerField(choices=STEP_TYPES)
    message = models.CharField(max_length=1000)
    options = models.CharField(max_length=500, blank=True, null=True)
