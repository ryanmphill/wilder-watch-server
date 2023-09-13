from rest_framework import serializers
from wilderwatch_api.models import WilderUserStudyObservation
from wilderwatch_api.serializers import WilderUserSerializer

class ObservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WilderUserStudyObservation
        fields = ('id', 'participant', 'study', 'latitude', 'longitude', 
                  'description', 'image', 'date', 'participant_name')
