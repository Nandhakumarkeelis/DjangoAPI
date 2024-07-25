from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Color
        fields= ['Color_Name']


class PersonSerializers(serializers.ModelSerializer):

    Color= ColorSerializers()

    class Meta:
        model= Person
        fields= '__all__'


    def validate(self, data):
        if data['Age']< 18:
            raise serializers.ValidationError('Age Should be Greater than 18')
        
        return data
    
class Loginserializers(serializers.ModelSerializer):

    username= serializers.CharField()
    password= serializers.CharField()
    
class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ["username", "email", "password"]

    username= serializers.CharField()
    email= serializers.EmailField()
    password= serializers.CharField()
    

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username= data['username']).exists():
                raise serializers.ValidationError("Username is Already Taken!")
            
        if data['email']:
            if User.objects.filter(email= data['email']).exists():
                raise serializers.ValidationError("Email is Already Taken!")

        return data
    def create(self, validated_data):
        user= User.objects.create(username= validated_data['username'], email= validated_data['email'], password= validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    

class Bookserializers(serializers.ModelSerializer):

    class Meta:
        model= Books
        fields= '__all__'