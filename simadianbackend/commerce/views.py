from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ItemSerializer, CategorySerializer, MassUploadFileSerializer, MessageSerializer, MassUploadSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Item, Category, MassUpload, Messages
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
    	try:
        	user = request.user
        	print(request.data)
        	serializers = ItemSerializer(data=request.data, partial=True)
        	serializers.initial_data["seller"] = user.pk
        	if serializers.is_valid():
        		serializers.save()
        		return Response(serializers.data)
        	return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    	except:
    		raise Http404


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

class MessageCreateApiView(APIView):
    '''
    Create Messages account
    '''
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            sender = request.user
            receiver = User.objects.get(username=request.data.get("receiver"))
            content = request.data.get("content")

            if receiver == sender:
                return Response({
                    'message': 'can\'t message yourself'
                })
            message = Messages(sender=sender, receiver=receiver, content=content)
            try:
                message.save()
                return Response(request.data)
            except:
                pass
            return Response({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise Http404

class MessagesSentApiView(APIView):
    '''
    List Messages sent
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            sender = request.user
            messages = Messages.objects.all().filter(sender=sender)

            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        except:
            raise Http404

class MessagesReceivedApiView(APIView):
    '''
    List Messages sent
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            receiver = request.user
            messages = Messages.objects.all().filter(receiver=receiver)

            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        except:
            raise Http404


class MessageDeleteApiView(APIView):
    '''
    CRUD on Messages model
    '''
    permission_classes = [IsAuthenticated]
  
    def delete(self, request, format=None):
        try:
            id = request.data.get("message_id")
            category = Messages.objects.get(pk=id)
            serializers = MessageSerializer(category)
            if(category):
                if(category.sender == request.user):
                    category.delete()
            
                    return Response(serializers.data)
            
            return Response({'message': 'unauthorized'})
        except:
            raise Http404


class MassFiles(APIView):
    '''
    Create Messages account
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = MassUploadSerializer

    def post(self, request):
        try:
            user = request.user
            data = request.FILES
            print(data)
            MassUpload(user=user, file=data.get("file")).save()
            return Response({
                "message": "Data"
            })
        except:
            return Response({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


class MassUploadListApiView(generics.GenericAPIView,
                       mixins.ListModelMixin):
    '''
    Return Mass Upload File List Api View
    '''
    queryset = MassUpload.objects.all()
    serializer_class = MassUploadFileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'uploaded_at']
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # List out the Item with given filter fields
        return self.list(request, *args, **kwargs)