from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.http import HttpResponse
# Create your views here.
class CaseViewsets(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class ProgramViewsets(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class GalleryFileViewsets(viewsets.ModelViewSet):
    queryset = GalleryFile.objects.all()
    serializer_class = GalleryFileSerializer
