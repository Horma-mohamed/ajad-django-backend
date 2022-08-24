from email.policy import default
from blog.serializers import UserSerializer
from rest_framework import   serializers
from django.contrib.auth.models import User
from .models import *
from main.serializers import *


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(many=False)
    album= AlbumSerializer(many=False)
    Thumb = serializers.ImageField(source='thumb')
    country = serializers.CharField(source='country.name')
    region = serializers.CharField(source='region.name')
    id = serializers.IntegerField(source='pk')
    class Meta:
        model = Case
        fields ='__all__'

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    icon_url = serializers.FileField(source='icon')
    class Meta:
        model= Program
        fields = '__all__'

class GalleryFileSerializer(serializers.HyperlinkedModelSerializer):
    h = serializers.IntegerField(source='get_image_size.h')
    w = serializers.IntegerField(source='get_image_size.w')
    file= serializers.CharField(source='file.url',default=None)
    class Meta:
        model= GalleryFile
        fields = '__all__'