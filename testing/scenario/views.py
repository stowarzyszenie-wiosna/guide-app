from django.shortcuts import render
from rest_framework import viewsets
from scenario.models import *
from scenario.serializers import *

class ScenarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Scenarios
    """
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
