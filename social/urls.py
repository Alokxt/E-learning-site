from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user-feed/',views.dash,name = "user-feed"),
    path('posts/',views.post_pic,name="post_pic"),
    path('follow_user/<int:user_id>/',views.follow_user,name = "follow_user"),
    path('unfollow_user/<int:user_id>/',views.unfollow_user,name = "unfollow_user"),
    path('followpage/<str:user_name>',views.profile_user,name="users_profile"),
    path('chatbox/<int:user_id>',views.chaat,name="chats"),
    path('msg/',views.chatbox,name="msgs"),
    path('search_result/',views.search_user,name="search_result"),
]
