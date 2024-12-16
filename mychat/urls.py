from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homechatpage/<str:Chatroom_name>/',views.chatpage,name="chat-pagehome"),
    path('chat/<str:username>/',views.get_or_create_chatroom,name="start-chat"),
    path('chat/room/<str:Chatroom_name>',views.chatpage,name="chatroom"),
]
