from rest_framework import serializers
from .models import Item


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'seller',
            'name',
            'description',
            'thumbnail1',
            'thumbnail2',
            'mobile_no',
            'country',
            'state',
            'city',
            'landmark',
            'category',
        )

    def create(self, validated_data):
        '''
        Method is called when serializers.save()
        '''
        item = MyUser.objects.create_user(
            seller=validated_data['seller'],
            name=validated_data['name'],
            description=validated_data['description'],
            thumbnail1=validated_data['thumbnail1'], 
            thumbnail2=validated_data['thumbnail2'],
            mobile_no=validated_data['mobile_no'],
            country=validated_data['country'],
            state=validated_data['state'],
            city=validated_data['city'],
            landmark=validated_data['landmark'],
            category=validated_data['category']
        )
        
        return item


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'seller',
            'buyer',
            'name',
            'description',
            'thumbnail1',
            'thumbnail2',
            'mobile_no',
            'country',
            'state',
            'city',
            'landmark',
            'category',
        )

    def create(self, validated_data):
        '''
        Method is called when serializers.save()
        '''
        item = MyUser.objects.create_user(
        	seller=validated_data['seller'],
            buyer=validated_data['buyer'],
            name=validated_data['name'],
            description=validated_data['description'],
            thumbnail1=validated_data['thumbnail1'], 
            thumbnail2=validated_data['thumbnail2'],
            mobile_no=validated_data['mobile_no'],
            country=validated_data['country'],
            state=validated_data['state'],
            city=validated_data['city'],
            landmark=validated_data['landmark'],
            category=validated_data['category']
        )
        
        return item