from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models  import *
from .serializers import *
def home(req):
    return HttpResponse('<h1 style=" font-family:sans-serif; font-weight:800 " >This is the home page!</h1>')

class PartnerViewsets(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer