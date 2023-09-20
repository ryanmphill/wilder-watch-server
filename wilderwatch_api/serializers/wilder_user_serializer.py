from rest_framework import serializers
from wilderwatch_api.models import WilderUser
from wilderwatch_api.serializers.user_serializer import UserSerializer
from wilderwatch_api.serializers.observation_serializer import ObservationSerializer

class WilderUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = WilderUser
        fields = ('id', 'user', 'bio', 'flair', 'image_url', 'is_researcher', 'full_name')
        depth = 1

class WilderUserObservationsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    observations = ObservationSerializer(many=True)
    
    class Meta:
        model = WilderUser
        fields = ('id', 'user', 'bio', 'flair', 'image_url', 'is_researcher', 'full_name', 
                  'observations', 'date_joined', 'observation_count', 'authored_studies_count',
                  'studies_participated_count')
        depth = 1
