from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class shopsy(models.Model):
    choice = [('st','study'),
              ('gm','gaming'),
              ('hm','health & madical'),
              ('fs','fasion'),
              ('tc','technology'),
              ('ms','merchendise'),]
    item_field = models.CharField(default=0,max_length=2,choices=choice)
    item_img = models.ImageField(null=True,blank=True,upload_to='shop/',)
    item_name = models.CharField(max_length=200)
    item_prize = models.IntegerField(default=0)
    prize = models.IntegerField(default=0)
    item_avail = models.BooleanField(default=True)
    def __str__(self):
        return self.item_name


class cartitem(models.Model):
    user = models.ForeignKey(User,related_name="items",on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(shopsy,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)




    


    
