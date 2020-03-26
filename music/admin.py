from django.contrib import admin
from .models import Album


class MusicAdmin(admin.ModelAdmin ):
    list_display=('artist','album_title', 'genre')


admin.site.register(Album, MusicAdmin)