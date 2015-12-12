from step.models import *

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
		fields = ('id', 'content')