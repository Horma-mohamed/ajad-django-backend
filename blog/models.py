from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField 

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    thumb = CloudinaryField()
    description = RichTextField()
    album = models.OneToOneField("main.Album", on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=50)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    category= models.ForeignKey('main.Category',on_delete=models.CASCADE)
    date = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return f"{self.author}-{self.title}"






class Comment(models.Model):
    author = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    article =  models.ForeignKey(Article,related_name='comments', on_delete=models.CASCADE)
    text = RichTextField()
    date = models.DateTimeField( auto_now_add=True)


    def __str__(self):
        return f"{self.article}-{self.author}"