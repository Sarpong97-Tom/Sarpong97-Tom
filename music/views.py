from django.http import HttpResponse
from django.shortcuts import render
from .models import Album, Song

# Create your views here.
def index(request):
    alnums= Album.objects.all()
    return HttpResponse("Testing music app page")

def show(request, album_id):
    return HttpResponse("Testing detail page"+str(album_id))