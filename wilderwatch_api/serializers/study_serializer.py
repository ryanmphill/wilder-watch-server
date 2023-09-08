from rest_framework import serializers
from wilderwatch_api.models import Study
from wilderwatch_api.serializers.wilder_user_serializer import WilderUserSerializer
from wilderwatch_api.serializers.study_type_serializer import StudyTypeSerializer
from wilderwatch_api.serializers.region_serializer import RegionSerializer
from wilderwatch_api.serializers.observation_serializer import ObservationSerializer

class StudySerializer(serializers.ModelSerializer):

    author = WilderUserSerializer(many=False)
    
    class Meta:
        model = Study
        fields = ('id', 'author', 'subject', 'summary', 'details', 'start_date', 'end_date',
                  'is_complete', 'study_type', 'region', 'image_url', 'observations')
        depth = 1
