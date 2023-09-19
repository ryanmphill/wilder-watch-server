from rest_framework import serializers
from wilderwatch_api.models import Study
from wilderwatch_api.serializers.wilder_user_serializer import WilderUserSerializer
from wilderwatch_api.serializers.observation_serializer import ObservationSerializer



class StudySerializer(serializers.ModelSerializer):

    author = WilderUserSerializer(many=False)
    observations = ObservationSerializer(many=True)
    
    class Meta:
        model = Study
        fields = ('id', 'title', 'author', 'subject', 'summary', 'details', 'start_date', 'end_date',
                  'is_complete', 'study_type', 'region', 'image_url', 'observations', 'average_longitude',
                  'average_latitude', 'furthest_longitude', 'furthest_latitude')
        depth = 1
