from rest_framework import serializers
from wilderwatch_api.models import WilderUserStudyObservation
from wilderwatch_api.serializers import wilder_user_serializer

class ObservationSerializer(serializers.ModelSerializer):

    participant = wilder_user_serializer(many=False)
    
    class Meta:
        model = WilderUserStudyObservation
        fields = ('id', 'participant', 'study', 'latitude', 'longitude', 
                  'description', 'image', 'date')
