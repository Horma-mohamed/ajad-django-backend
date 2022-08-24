from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,PermissionsMixin ,BaseUserManager
from cloudinary.models import CloudinaryField
# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email,username,first_name,last_name,password):
        user = self.create_user( email,username,first_name,last_name,password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        
        if user.is_staff is not True:
            raise ValueError(_(" Superuser must be assigned to is_staff = True "))
        if user.is_superuser is not True:
            raise ValueError(_(" Superuser must be assigned to is_superuser = True "))
        user.save()
        return user

    def create_user(self, email,username,first_name,last_name,password):
        if not email :
            raise ValueError(_(" You must provide an email adress "))
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,first_name=first_name,last_name=last_name )
        user.set_password(password)
        user.save()
        return user

    
class CostumUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    phone = models.IntegerField(blank=True,null=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, unique=False)
    last_name = models.CharField(max_length=40, unique=False)
    join_date = models.DateTimeField( auto_now_add=True)
    profile_img = CloudinaryField()
    bio = RichTextField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username','first_name','last_name']

class Album(models.Model):
    TYPES=[
        ('Image',"Image"),
        ('Video',"Video"),
    ]
    type = models.CharField( max_length=50,choices=TYPES,default=1)
    name=models.CharField(max_length=50,default=f'album-')
    def __init(self):
        self.name = f'album-{self.pk}'
    def __str__(self):
        return f'Album-{self.id}'

class Image(models.Model):
    image = CloudinaryField()
    album = models.ForeignKey("main.Album",related_name='images', on_delete=models.DO_NOTHING)

class Category(models.Model):
    name = models.CharField( max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=255)
    icon = CloudinaryField()
    def __str__(self):
        return self.name
    

class Country(models.Model):
    name = models.CharField( max_length=250)

    def __str__(self):
        return self.name

class Region(models.Model):
    name= models.CharField( max_length=250)
    country = models.ForeignKey("main.Country", on_delete=models.CASCADE)

    def __str__(self):
        return self.name