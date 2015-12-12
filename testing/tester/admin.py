from django.contrib import admin
from tester.models import *

# Register your models here.

@admin.register(Tester)
class TesterAdmin(admin.ModelAdmin):
    pass