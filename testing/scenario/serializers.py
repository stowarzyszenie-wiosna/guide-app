from scenario.models import *
from rest_framework import *

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ('id', 'name', 'site_url', 'created')
