from django.http import HttpResponse
from django.shortcuts import render
from blog.serializers import *
from rest_framework import  viewsets
from .models import *

# Create your views here.

class ArticleViewsets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def blog(req):
    return HttpResponse('Home')