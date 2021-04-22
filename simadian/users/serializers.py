from rest_framework import serializers
from .models import MyUser, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'email',
            'password'
        )

    def create(self, validated_data):
        '''
        Method is called when serializers.save()
        '''
        user = MyUser.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'], 
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        depth = 2
        fields = (
            'profile',
            'profile_pic',
        )
