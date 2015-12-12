from django.db import models


class Scenario(models.Model):
    name = models.CharField(max_length=100)
    site_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
