from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    title = models.CharField(max_length=200)
    news_des = HTMLField()

    

# Create your models here.
