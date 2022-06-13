from django.contrib import admin
from .models import Page, Pointcloud, customisation

# Register your models here.

admin.site.register(Page)
admin.site.register(Pointcloud)
admin.site.register(customisation)