from django.db import models
from django.contrib.auth.models import User
from bunch.models import Profile
import shortuuid


class ChatGroup(models.Model):
    group_name = models.CharField(max_length=250,unique=True,default=shortuuid.uuid)
    users_online = models.ManyToManyField(User,related_name="users_online",blank=True)
    members = models.ManyToManyField(Profile,related_name="chat_groups",blank=True)
    is_private = models.BooleanField(default=False)

    

    def __str__(self):
        return self.group_name
    

class Groupmessage(models.Model):
    group = models.ForeignKey(ChatGroup,related_name='chat_messages',on_delete=models.CASCADE)
    author= models.ForeignKey(Profile,on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.user.username} :{self.body}'
    
    class Meta:
        ordering = ['-created']
