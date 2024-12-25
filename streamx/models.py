from django.db import models
import PIL
from bunch.models import cours

# Create your models here.
class Coursevideos(models.Model):
    course = models.ForeignKey(cours,on_delete=models.CASCADE,default=None)
    video_title = models.CharField(max_length=250,default="Untitiled-vd")
    video_thumbnail = models.ImageField(upload_to='media/',blank=True)
    video = models.FileField(upload_to='videos/')
    video_description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    course = models.ForeignKey(cours,on_delete=models.CASCADE,default=None)
    video_list = models.ManyToManyField(Coursevideos)
    Playlist_name = models.CharField(max_length=350)
    