from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class ImageAdmin(admin.StackedInline):
    model = Image
    extra=0

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    inlines = [ImageAdmin,]

admin.site.register(Album)
admin.site.register(Partner)
admin.site.register(Image)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CostumUser,UserAdmin)
