from django.shortcuts import render,redirect
from mychat.models import ChatGroup
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
@login_required
def follow_user(request,user_id):
    user_to_follow = get_object_or_404(User, id= user_id)
    if request.user != user_to_follow:
        Follow.objects.get_or_create(followers = request.user , followings = user_to_follow)
        
        messages.success(request,f'You are now following {{user_to_follow.username}}')
    else:
        messages.success(request,f'You cannot follow yourself')
    return redirect('users_profile',user_id = user_id)

@login_required
def unfollow_user(request,user_id):
    user_to_unfollow = get_object_or_404(User,id=user_id)
    Follow.objects.filter(followers = request.user,followings = user_to_unfollow).delete()
    messages.success(request,f'You unfollowedd {{user_to_unfollow.username}}')
    return redirect('users_profile',user_id=user_id)

@login_required
def post_pic(request):
    if request.method == 'POST':
        
        post_form = Postform(request.POST,request.FILES)
        if post_form.is_valid():
            post_instance = post_form.save(commit=False) 
            post_instance.user = request.user  
            post_instance.save()  
            
            #user_post = post_form.cleaned_data.get('post_pic')
            #post_caption = post_form.cleaned_data.get('caption')
            #print(post_caption)
            #print(user_post)
            #post.objects.create(user = request.user,post_pic=user_post,caption = post_caption)
            messages.success(request,f'image posted successefully')
            return redirect('user-feed')
    else:
        post_form = Postform()
    context = {'postform':post_form}
    return render(request,'postform.html',context)
@login_required
def dash(request):
    posts = post.objects.filter(user = request.user)
    user_following = Follow.objects.filter(followers = request.user)
    m =[]
    for obj in user_following:
        photo = post.objects.filter(user = obj.followings.id)
        for p in photo:
            print(p.post_pic)
            m.append(p)

    print(m)
   
    accounts = Profile.objects.all().exclude(user = request.user)
    context = {'posts':posts,'accounts':accounts,'feed':m}
    return render(request,'social_dash.html',context)
def isfollowing(follower,following):
    return Follow.objects.filter(followers=follower,followings = following).exists()

@login_required
def profile_user(request,user_name):
    user_pro = get_object_or_404(User,username = user_name)
    user_proil = Profile.objects.get(user = user_pro)
    print(user_pro)
    key = isfollowing(request.user,user_pro)
    posts = post.objects.filter(user = user_pro)
    posts_pic = []
    for obj in posts:
        posts_pic.append(obj)
    print(posts)
    print(key)
    print(posts_pic)
    #if key:
    #    unfollow = unfollow_user(request,user_id = user_id)
    #else:
    #    follow = follow_user(request,user_id=user_id)
    context = {'user_pro':user_pro,'dp':user_proil,'key':key,'posts':posts_pic}

    return render(request,'followpage.html',context)

@login_required
def chaat(request,user_id):
    user_to_msg = get_object_or_404(User,id = user_id)
    chatter =get_object_or_404(User,id = request.user.id)

    texts = messaging.objects.filter(sender = request.user,receiver = user_to_msg)
    texts2 = messaging.objects.filter(sender = user_to_msg,receiver =request.user)

    

    sms = texts.order_by("time")
    sms1 = texts2.order_by("time")
    m = []
    
    for ss in sms:
        m.append(ss)
    for ss in sms1:
        m.append(ss)
    
    m = sorted(m,key = lambda messaging:messaging.time )
    print(m)
    if request.method == "POST":
        chat = chatForm(request.POST,instance=request.user)
        if chat.is_valid():
            sms = chat.cleaned_data.get('msg')
            message = messaging.objects.create(sender = request.user,receiver = user_to_msg,msg = sms)
            print(sms)
            print(message)
            
            chat = chatForm()
            context = {'msg':texts,'opposite':texts2,'chatting':user_to_msg,'chat':chat}
            return redirect('chats',user_id = user_id)
    else:
        chat = chatForm()
    context = {'msg':texts,'opposite':texts2,'chat':chat,'chatting':user_to_msg,'chatter':chatter,'chatting':m}
    return render(request,'chatbox.html',context)


def chatbox(request):
    usr = Follow.objects.filter(followers = request.user)
    form = ChatGroupForm()
    if(request.method == "POST"):
        form = ChatGroupForm(request.POST)
        if(form.is_valid()):
           my_group = form.cleaned_data.get("Group_name")
           my_members = form.cleaned_data.get("members")
           group = ChatGroup.objects.create(group_name = my_group)
           group.members.add(*my_members) 
    userc = Profile.objects.get(user = request.user)
    gourps = ChatGroup.objects.filter(members = userc,is_private=False)
    print(gourps)
    l = []
    for obj in gourps:
        l.append(obj)
    context = {'chats':usr,'groups':l,'groupform':form}
    
    return render(request,'messages.html',context)
    


def search_user(request):
    query = request.GET.get('q','')
    userp =[]
    if(query):
        user1 = User.objects.filter(username__icontains = query)
        userp = Profile.objects.filter(user__in = user1).values('id','user__username')

    return JsonResponse({'results':list(userp)})





        


# Create your views here.
