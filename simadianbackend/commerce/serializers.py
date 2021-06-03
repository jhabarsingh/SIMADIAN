from rest_framework import serializers
from .models import Item, Category, Messages, MassUpload

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
        	'id',
            'seller',
            'buyer',
            'category',
            'name',
            'description',
            'writer',
            'thumbnail1',
            'thumbnail2',
            'cost_price',
            'sell_price',
            'sold',
            'mobile_no',
            'country',
            'state',
            'city',
            'landmark',
            'educational_institution'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        depth = 3
        fields = (
            'id',
            'sender',
            'receiver',
            'content'
        )

class MassUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MassUpload
        depth = 3
        fields = (
            'file',
        )


class MassUploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MassUpload
        depth = 1
        fields = (
            'user',
            'file',
            'uploaded_at'
        )
