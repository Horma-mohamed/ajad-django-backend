from rest_framework import routers , serializers , viewsets
from main.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username',]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name','slug',]

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image',]

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id','images',]

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    icon_url = serializers.ImageField(source='icon')
    class Meta:
        model = Partner
        fields = '__all__'