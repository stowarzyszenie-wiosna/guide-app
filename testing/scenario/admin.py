from django.contrib import admin
from scenario.models import *


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    pass
