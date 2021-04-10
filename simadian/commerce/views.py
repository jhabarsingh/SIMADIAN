from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ItemSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Item, Category
from django.http import Http404
from rest_framework import status

User = get_user_model()


class ItemListApiView(generics.GenericAPIView,
                       mixins.ListModelMixin):
    '''
    Return all the users avaialble if  their account
    filters are available
    '''
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name', 'sold', 'country', 'city', 'state', 'landmark']

    def get(self, request, *args, **kwargs):
        # List out the Item with given filter fields
        return self.list(request, *args, **kwargs)


class ItemCreateApiView(generics.CreateAPIView):
    '''
    Create Item account
    '''
    serializer_class = ItemSerializer


class CategoryCreateApiView(generics.CreateAPIView):
    '''
    Create Item account
    '''
    serializer_class = CategorySerializer


class ItemUpdateDeleteApiView(APIView):
    '''
    CRUD on Item model
    '''
    permission_classes = [IsAuthenticated]
  
    def put(self, request, format=None):
        try:
            user = request.user
            serializers = UserSerializer(buyer=user, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        try:
            id = request.data.get("id")
            item = Item.objects.get(pk=id)
            serializers = ItemSerializer(item)
            item.delete()
            return Response(serializers.data)
        except Profile.DoesNotExist:
            raise Http404

class CategoryUpdateApiView(APIView):
    '''
    CRUD on Item model
    '''
    permission_classes = [IsAuthenticated]
  
    def put(self, request, format=None):
        try:
            serializers = CategorySerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        try:
            id = request.data.get("id")
            category = Category.objects.get(pk=id)
            serializers = Category(category)
            category.delete()
            return Response(serializers.data)
        except Profile.DoesNotExist:
            raise Http404
