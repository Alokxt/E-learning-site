from django.shortcuts import render
from .models import *
# Create your views here.
def dashboard(request):
    vds = Coursevideos.objects.all()[:20]
    return render(request,'latest_uploadvideo.html',{'obj':vds})


def videoplaying(request,vide_id):
    vd = Coursevideos.objects.get(id = vide_id)
    return render(request,'video_playing.html',{'vid':vd})