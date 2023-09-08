from rest_framework import serializers
from wilderwatch_api.models import Region

class RegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Region
        fields = ('id', 'label')
