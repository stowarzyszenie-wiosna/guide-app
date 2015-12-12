from django.contrib import admin
from scenario.models import *


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    pass
