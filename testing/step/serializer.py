from step.models import *

class StepSerializer(serializers.ModelSerializer):


	fields = ('email', 'username', 'password')
	
	
    class Meta:
        model = Step