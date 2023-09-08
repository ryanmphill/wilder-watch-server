from rest_framework import serializers
from wilderwatch_api.models import WilderUser
from wilderwatch_api.serializers.user_serializer import UserSerializer

class WilderUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = WilderUser
        fields = ('id', 'user', 'bio', 'flair', 'image_url', 'is_researcher', 'full_name')
        depth = 1

class WilderUserObservationsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    class Meta:
        model = WilderUser
        fields = ('id', 'user', 'bio', 'flair', 'image_url', 'is_researcher', 'full_name', 
                  'observations')
        depth = 1