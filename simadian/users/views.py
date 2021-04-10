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


class UsersListApiView(generics.GenericAPIView,
                       mixins.ListModelMixin):
    '''
    Return all the users avaialble if  their account
    filters are available
    '''
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'email', 'username']

    def get(self, request, *args, **kwargs):
        # List out the user with given username
        return self.list(request, *args, **kwargs)


class UserCreateApiView(generics.CreateAPIView):
    '''
    Create Users account
    '''
    serializer_class = UserSerializer
    

class UserRetrieveUpdateDeleteApiView(
            generics.GenericAPIView,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin):
    '''
    CRUD on user model
    '''
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    url_kwarg = 'username'
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Retrieve the user with given username
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        # Update the user with given username
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        # Delete the user with given username
        return self.destroy(request, *args, **kwargs)