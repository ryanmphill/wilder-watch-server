from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError
from wilderwatch_api.models import (Study, WilderUser, Region, StudyType, WilderUserStudyObservation)
from wilderwatch_api.serializers import (StudySerializer, ObservationSerializer)

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
    
    def update(self, request, pk):
        """Update a study"""

        try:
            region = Region.objects.get(pk=request.data['regionId'])
            study_type_instance = StudyType.objects.get(pk=request.data['studyTypeId'])
            image_url = "https://images.unsplash.com/photo-1619468129361-605ebea04b44?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80"

            if len(request.data['imageUrl']) > 0:
                image_url = request.data['imageUrl']
            end_date = request.data['endDate']
            if len(end_date) == 0:
                end_date = None
            
            current_wilder_user = WilderUser.objects.get(user=request.auth.user)

            study = Study.objects.get(
                pk=pk)
            
            if study.author == current_wilder_user:
            
                study.title=request.data['title']
                study.subject=request.data['subject']
                study.summary=request.data['summary']
                study.details=request.data['details']
                study.start_date=request.data['startDate']
                study.end_date=end_date
                study.study_type=study_type_instance
                study.region=region
                study.image_url=image_url

                study.save()
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': "You can only edit your own studies"}, status=status.HTTP_403_FORBIDDEN)

        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Study.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except KeyError as ex:
            return Response({'message': f"{ex.args[0]} is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        """Delete a Study"""
        try:
            current_wilder_user = WilderUser.objects.get(user=request.auth.user)

            study = Study.objects.get(
                pk=pk)
            if study.author == current_wilder_user:
                study.delete()
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': "You can only delete your own studies"}, status=status.HTTP_403_FORBIDDEN)
        except Study.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    @action(methods=['post'], detail=True)
    def add_observation(self, request, pk):
        """Add an observation to the selected study"""
        try:
            participant = WilderUser.objects.get(user=request.auth.user)
            study = Study.objects.get(pk=pk)

            observation = WilderUserStudyObservation.objects.create(
                participant=participant,
                study=study,
                latitude=request.data['latitude'],
                longitude=request.data['longitude'],
                description=request.data['description'],
                image=request.data['image'],
                date=request.data['date']
            )
            serializer = ObservationSerializer(observation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as ex:
            return Response({'message': f"{ex.args[0]} is required"}, status=status.HTTP_400_BAD_REQUEST)
