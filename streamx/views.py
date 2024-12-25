from django.shortcuts import render
from .models import *
# Create your views here.
def dashboard(request):
    vds = Coursevideos.objects.all()[:20]
    return render(request,'latest_uploadvideo.html',{'obj':vds})