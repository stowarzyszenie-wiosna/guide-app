from django.contrib import admin
from step.models import *

# Register your models here.

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    pass