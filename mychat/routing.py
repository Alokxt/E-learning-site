from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path("ws/homechatpage/<str:Chatroom_name>",consumers.Chatroomconsumer.as_asgi()),
]