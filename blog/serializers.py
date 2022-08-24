from rest_framework import routers , serializers , viewsets
from .models import *
from main.models import *
from main.serializers import *


#from .serializers import ArticleSerializer 




class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(many=False)
    author_name=serializers.CharField(source='author.username')
    class Meta:
        model = Comment
        fields =[ 'author','text','date','author_name']



class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    album= AlbumSerializer(many=False)
    author = UserSerializer(many=False)
    author_name=serializers.CharField(source='author.username')
    comments = CommentSerializer(many=True)
    category = CategorySerializer(many=False)
    id = serializers.IntegerField(source='pk')
    Thumb = serializers.ImageField(source='thumb')
    class Meta:
        model = Article
        fields = '__all__'






