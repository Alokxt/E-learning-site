from django.contrib import admin
from social.models import *

# Register your models here.
admin.site.register(user_profile)
admin.site.register(post)
admin.site.register(messaging)
admin.site.register(Follow)