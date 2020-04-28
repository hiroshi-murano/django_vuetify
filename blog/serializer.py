from rest_framework import serializers

from .models import User, Entry, Syain,Syain2


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'mail')

    # def create(self, validated_data):

    #     User = User.objects.create(**validated_data)
    #     for item in validated_data:
    #         User.objects.create(User=User, **item)
    #     return User


class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書き
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')


class SyainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syain
        fields = ('id','name', 'age', 'weight', 'birthday')


class Syain2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Syain2
        fields = ('id','name', 'age', 'weight', 'birthday')

