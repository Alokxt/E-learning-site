from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from shopp.models import shopsy

class cours(models.Model):
    choice = [
        ('WD','web development'),
        ('AD','App development'),
        ('ML','Machine learning'),
        ('AI','Artificial intelligence'),
        ('DS','Data science'),
        ('CS','Cyber security'), ]
    course_name = models.CharField(max_length=50)
    course_image = models.ImageField(upload_to= 'courses/',null= True,blank=True)
    course_des = models.CharField(max_length=300)
    course_release = models.DateTimeField(default=timezone.now)
    course_field = models.CharField(default= 0,max_length=2,choices=choice)
    def __str__(self):
        return self.course_name
# Create your models here.

class todo(models.Model):
    user = models.ForeignKey(User,default = None,on_delete=models.CASCADE)
    work = models.ForeignKey(cours,on_delete=models.CASCADE)
    completed = models.BooleanField(default= False)

class Profile(models.Model):
    user = models.OneToOneField(User,default=None,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    since_on = models.DateTimeField(default=timezone.now)
    orders = models.ManyToManyField(shopsy)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_photo:
            img = Image.open(self.profile_photo.path)

            if img.height >300 or img.width>300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.profile_photo.path)


