from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError
from wilderwatch_api.models import (Study, WilderUser, Region, StudyType)
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
    
    def create(self, request):
        """Create a new Study"""
        
        try:
            author = WilderUser.objects.get(user=request.auth.user)
            region = Region.objects.get(pk=request.data['regionId'])
            study_type = StudyType.objects.get(pk=request.data['studyTypeId'])
            image_url = "https://images.unsplash.com/photo-1619468129361-605ebea04b44?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80"
            if len(request.data['imageUrl']) > 0:
                image_url = request.data['imageUrl']
            end_date = request.data['endDate']
            if len(end_date) == 0:
                end_date = None

            study = Study.objects.create(
                author=author,
                title=request.data['title'],
                subject=request.data['subject'],
                summary=request.data['summary'],
                details=request.data['details'],
                start_date=request.data['startDate'],
                end_date=end_date,
                is_complete=False,
                study_type=study_type,
                region=region,
                image_url=image_url
            )
            serializer = StudySerializer(study)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as ex:
            return Response({'message': f"{ex.args[0]} is required"}, status=status.HTTP_400_BAD_REQUEST)