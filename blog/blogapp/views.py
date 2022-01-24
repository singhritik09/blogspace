from django.shortcuts import render
from .models import Video
# Create your views here.

def vdo(request):
    video=Video.objects.all()
    
    return render(request,"videos.html",{"video":video})

def home(request):
    return render(request,"index.html")