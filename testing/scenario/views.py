from scenario.models import *
from scenario.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def scenario_detail(request, scenario_pk, format=None):
    obj = get_object_or_404(Scenario, pk=scenario_pk)
    return Response(ScenarioSerializer(obj).data)

@api_view(['GET'])
def group_detail(request, scenario_pk, site_url, format=None):
    obj = get_object_or_404(Group, scenario__pk=scenario_pk, site_url=site_url)
    return Response(GroupSerializer(obj).data)
