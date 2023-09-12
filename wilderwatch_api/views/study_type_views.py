from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from wilderwatch_api.models import ( StudyType )
from wilderwatch_api.serializers import ( StudyTypeSerializer )

class StudyTypeView(ViewSet):
    """Handle requests for study types
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request):
        """Get a list of all study types
        """
        study_types = StudyType.objects.all()
        serializer = StudyTypeSerializer(study_types, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Get a single study type"""
        try:
            study_type = StudyType.objects.get(pk=pk)
            serializer = StudyTypeSerializer(study_type)
            return Response(serializer.data)
        except StudyType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
