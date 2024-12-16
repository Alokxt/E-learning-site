from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bunch.models import Profile


class user_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    profile_photo = models.ForeignKey(Profile,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    


class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    post_pic = models.ImageField(upload_to='posts',null=True,blank=True)
    posted = models.DateTimeField(default=timezone.now)
    caption = models.TextField()

class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_pic = models.ForeignKey(post,on_delete=models.CASCADE)

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_pic = models.ForeignKey(post,on_delete=models.CASCADE)
    text = models.TextField()
    created = models.TimeField()

class Follow(models.Model):
    following_count = models.IntegerField(default=0)
    followings = models.ForeignKey(User,related_name='following',on_delete=models.CASCADE)
    followers = models.ForeignKey(User,related_name='followers',on_delete=models.CASCADE)
    follower_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('followers','followings')

class messaging(models.Model):
    msg = models.TextField()
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender',default=None)
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver',default=None)
    time = models.DateTimeField(default=timezone.now)
    read_reciept = models.BooleanField(default=False)

    






# Create your models here.
