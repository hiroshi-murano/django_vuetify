from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from .models import User, Entry, Syain, Syain2
from .serializer import UserSerializer, EntrySerializer, SyainSerializer, Syain2Serializer
from rest_framework.response import Response
from rest_framework import status


# Django REST Frameworkを使って爆速でAPIを実装する
# https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8 参照
# https://arakan-pgm-ai.hatenablog.com/entry/2019/06/17/000000 参照(CORS対策)


class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()

    # 一度に複数をpostするためのオーバーライド
    # Django Rest Framework create multiple objects
    # https://stackoverflow.com/questions/54059415/django-rest-framework-create-multiple-objects/54061655　参照
    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = UserSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author', 'status')


class SyainViewSet(viewsets.ModelViewSet):

    serializer_class = SyainSerializer
    model = Syain
    queryset = Syain.objects.all()

    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = SyainSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Syain2ViewSet(viewsets.ModelViewSet):

    queryset = Syain2.objects.all()
    serializer_class = Syain2Serializer
