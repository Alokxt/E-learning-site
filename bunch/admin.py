from django.contrib import admin
from .models import cours,Profile
from django.contrib.auth.models import User

admin.site.register(cours)
admin.site.register(Profile)

# Register your models here.
