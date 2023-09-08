from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from wilderwatch_api.models import (Study)
from wilderwatch_api.serializers import (StudySerializer)

class StudyView(ViewSet):
    """Handle requests for studies
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request):
        """Get a list of all studies
        """
        studies = Study.objects.all()
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Get a single study"""
        try:
            study = Study.objects.get(pk=pk)
            serializer = StudySerializer(study)
            return Response(serializer.data)
        except Study.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)