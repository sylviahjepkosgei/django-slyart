
from django.contrib import admin
from .models import Category,Location,Image
class ImageAdmin(admin.ModelAdmin):
    

    admin.site.register(Category)
    admin.site.register(Image)
    admin.site.register(Location)