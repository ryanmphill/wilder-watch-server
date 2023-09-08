from rest_framework import serializers
from wilderwatch_api.models import StudyType

class StudyTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudyType
        fields = ('id', 'label')
