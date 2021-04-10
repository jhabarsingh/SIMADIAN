from rest_framework import serializers
from .models import Item, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'seller',
            'buyer',
            'category',
            'name',
            'description',
            'thumbnail1',
            'thumbnail2',
            'sold',
            'mobile_no',
            'country',
            'state',
            'city',
            'landmark',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category',
        )
