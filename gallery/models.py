from asyncio.windows_events import NULL
from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
import cv2
from PIL import Image as img
from io import BytesIO
import requests

from main.models import Country, Region
User = get_user_model()
# Create your models here.
class Program(models.Model):
    name = models.CharField( max_length=50)
    icon = CloudinaryField(null=True,blank=True)
    intro = RichTextField()
    description = RichTextField()
    def __str__(self):
        return self.name
class Case(models.Model):
    title = models.CharField( max_length=50)
    intro = models.TextField(max_length=300)
    description = RichTextField()
    thumb = CloudinaryField()
    author = models.ForeignKey(User,related_name='cases' ,on_delete=models.CASCADE)
    programs= models.ManyToManyField("gallery.Program",related_name='cases',blank=True,null=True)
    album = models.OneToOneField("main.Album", on_delete=models.DO_NOTHING)
    date = models.DateTimeField( auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class GalleryFile(models.Model):
    TYPES=[
        ('Image',"Image"),
        ('Video',"Video"),
    ]
    type = models.CharField( max_length=50,choices=TYPES,default=1)
    file = CloudinaryField(blank=True,null=True)
    link = models.CharField( max_length=255,blank=True,null=True)
    def get_image_size(self):
        if self.type == 'Image':
            rep = requests.get(self.file.url)
            i = img.open(BytesIO(rep.content))
            width,hieght = i.size
            return {
                'h':hieght,
                'w':width,
            }
        else:
            self.file = None
            return {
                'h':None,
                'w':None,
            }
    def __str__(self):
            return f"File-{self.pk}"

    





