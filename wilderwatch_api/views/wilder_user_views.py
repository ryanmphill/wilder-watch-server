from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError
from wilderwatch_api.models import ( WilderUser )
from wilderwatch_api.serializers import ( WilderUserSerializer, WilderUserObservationsSerializer )

class WilderUserView(ViewSet):
    """Handle requests for users
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request):
        """Get a list of all users
        """
        wilder_users = WilderUser.objects.all()
        serializer = WilderUserSerializer(wilder_users, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Get a single user"""
        try:
            wilder_user = WilderUser.objects.get(pk=pk)
            serializer = WilderUserObservationsSerializer(wilder_user)
            return Response(serializer.data)
        except WilderUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    
    @action(methods=['get'], detail=False)
    def current(self, request):
        """Get the current user based on auth token"""
        try:
            current_wilder_user = WilderUser.objects.get(user=request.auth.user)
            serializer = WilderUserSerializer(current_wilder_user)
            return Response(serializer.data)
        except WilderUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
