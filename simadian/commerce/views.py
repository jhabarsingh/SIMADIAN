from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ItemSerializer, CategorySerializer, MessageSerializer
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
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # List out the Item with given filter fields
        return self.list(request, *args, **kwargs)


class CategoryListApiView(generics.GenericAPIView,
                       mixins.ListModelMixin):
    '''
    Return all the category avaialble 
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    authentication_classes = []
    pagination_class = None

    def get(self, request, *args, **kwargs):
        # List out the Item with given filter fields
        return self.list(request, *args, **kwargs)


class CategoryCreateApiView(generics.CreateAPIView):
    '''
    Create Item account
    '''
    serializer_class = CategorySerializer


class ItemCreateApiView(APIView):
    '''
    Create Item account
    '''

    def post(self, request):
    	# try:
    	user = request.user
    	print(request.data)
    	serializers = ItemSerializer(data=request.data, partial=True)
    	serializers.initial_data["seller"] = user.pk
    	if serializers.is_valid():
    		serializers.save()
    		return Response(serializers.data)
    	return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    	# except:
    		# raise Http404


class ItemUpdateDeleteApiView(APIView):
    '''
    CRUD on Item model
    '''
    permission_classes = [IsAuthenticated]
  
    def put(self, request, format=None):
        try:
            id = request.data.get("id")
            item = Item.objects.get(pk=id)
            serializers = ItemSerializer(item, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
        	raise Http404

    def delete(self, request, format=None):
        try:
            id = request.data.get("id")
            item = Item.objects.get(pk=id)
            serializers = ItemSerializer(item)
            item.delete()
            return Response(serializers.data)
        except:
        	raise Http404

class CategoryDeleteApiView(APIView):
    '''
    CRUD on Item model
    '''
    permission_classes = [IsAuthenticated]
  
    def delete(self, request, format=None):
        try:
            id = request.data.get("category")
            category = Category.objects.get(pk=id)
            serializers = CategorySerializer(Category.objects.get(pk=id))
            category.delete()
            return Response(serializers.data)
        except:
        	raise Http404
