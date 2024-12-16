from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from.models import *
from django.http import Http404
from .form import *
from django.contrib.auth.decorators import login_required
from bunch.models import Profile

# Create your views here.
@login_required
def chatpage(request,Chatroom_name = "public-chat"):
    chatgrp = get_object_or_404(ChatGroup,group_name=Chatroom_name)
    chtmsg = chatgrp.chat_messages.all()[:80]
    form = GroupChatMessage()

    other_user=None
    if chatgrp.is_private:
        userc = Profile.objects.get(user = request.user)
        if userc not in chatgrp.members.all():
            raise Http404
        for member in chatgrp.members.all():
            if member != userc:
                other_user = member
                break


   
    if(request.htmx):
        
        form = GroupChatMessage(request.POST)
        if(form.is_valid()):
            message = form.save(commit=False)
            message.group = chatgrp
            print(message.group)
            message.author = get_object_or_404(Profile,user=request.user)
            message.save()
            context ={
                'message':message,
                'user':request.user
            }
            return render(request,'partials/chat_message_p.html',context)
    context = {
        'chat_messages':chtmsg,'form':form,
        'other_user':other_user,
        'chatroom_name':Chatroom_name,
    }
    return render(request,'chat.html',context)

@login_required
def get_or_create_chatroom(request,username):
    if(request.user.username == username):
        return redirect('chat-pagehome')
    other_userp = User.objects.get(username=username)
    other_user = Profile.objects.get(user = other_userp)
    curr_user = Profile.objects.get(user = request.user)
    user1 = get_object_or_404(Profile,user = request.user)
    my_chatroom = ChatGroup.objects.filter(is_private = True,members=user1)
    if(my_chatroom):
        for chatroom in my_chatroom:
            if(other_user in chatroom.members.all()):
                chatroom = chatroom
                break;
            else:
                chatroom = ChatGroup.objects.create(is_private = True)
                chatroom.members.add(curr_user,other_user)
    else:
        chatroom = ChatGroup.objects.create(is_private = True)
        chatroom.members.add(curr_user,other_user)
    
    return redirect('chatroom',chatroom.group_name)



