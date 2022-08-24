from django.contrib import admin

from main.admin import ImageAdmin
from .models import *
# Register your models here.



class CaseAdmin(admin.ModelAdmin):
    model = Case
   

admin.site.register(Case,CaseAdmin)
admin.site.register(Program)
admin.site.register(GalleryFile)
