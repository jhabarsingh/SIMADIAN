from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Profile
from django.http import Http404
from rest_framework import status

User = get_user_model()

class UsersListApiView(generics.GenericAPIView,
                       mixins.ListModelMixin):
    '''
    Return all the users avaialble if  their account
    filters are available
    '''
    queryset = get_user_model().objects.all().order_by('username')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'email', 'username']
    ordering = ['username']
    paginate_by = 20
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # List out the user with given username
        return self.list(request, *args, **kwargs)


class UserCreateApiView(generics.CreateAPIView):
    '''
    Create Users account
    '''
    serializer_class = UserSerializer
    authentication_classes = []

class ProfileRetrieveUpdateDeleteApiView(APIView):  
    '''
    Create Users Profile
    '''
    permission_classes = [IsAuthenticated]
  
    def get(self, request, format=None):
        try:
            profile = Profile.objects.get(profile=request.user)
            serializers = ProfileSerializer(profile)
            return Response(serializers.data)
        except Profile.DoesNotExist:
            raise Http404
  
    def put(self, request, format=None):
        try:
            profile = Profile.objects.get(profile=request.user)
            serializers = ProfileSerializer(profile, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            raise Http404

    

class UserRetrieveUpdateDeleteApiView(APIView):
    '''
    CRUD on user model
    '''
    permission_classes = [IsAuthenticated]
  
    def get(self, request, format=None):
        try:
            user = request.user
            serializers = UserSerializer(user)
            return Response(serializers.data)
        except Profile.DoesNotExist:
            raise Http404
  
    def put(self, request, format=None):
        try:
            user = request.user
            serializers = UserSerializer(user, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        try:
            profile = request.user
            user = request.user
            serializers = UserSerializer(user)
            profile.delete()
            return Response(serializers.data)
        except Profile.DoesNotExist:
            raise Http404
