from django.contrib import admin
from .models import MainImage

class MainImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'type')


admin.site.register(MainImage, MainImageAdmin)
