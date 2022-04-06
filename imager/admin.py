from django.contrib import admin

from .models import Imager

@admin.register(Imager)
class ImagerAdmin(admin.ModelAdmin):
    list_display = ['name','description','user','image','date','time']
