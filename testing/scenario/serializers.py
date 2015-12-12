from rest_framework import serializers
from scenario.models import *


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'position', 'type', 'message', 'options')


class GroupSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'site_url', 'steps')


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ('id', 'name', 'created')
