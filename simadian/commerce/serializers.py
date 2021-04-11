from rest_framework import serializers
from .models import Item, Category


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
