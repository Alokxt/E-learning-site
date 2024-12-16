from django.shortcuts import render,redirect,HttpResponse
from .import views
from news.models import News
from django.contrib import messages
from asgiref.sync import sync_to_async
from .models import cours
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from .models import todo




# Create your views here.

'''def login_view(request):
    if(request.method == "POST"):
       usernamec = request.POST.get('username')
       passw = request.POST.get('pass')
       user = authenticate(request,username = usernamec,password = passw)
       if(user is not None):
              login(request,user)
              ans2 = "HELLO" + usernamec
              o = {'name': ans2}

              return redirect('dashboard')
       
       else:
            d = {}
            ans = "wrong password or username"
            d = {'warn':ans}
            return render(request,'login.html',d)

        
    return render(request,'login.html') '''

def login_view(request):
    #profile = Profile(user = request.user)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1 == pass2 :
                my_user = form.save(commit=False)
                #my_user = User.objects.create_user(user_name,pass1,email)
                my_user.save()
                return redirect('/')
            else:
                messages.success(request,f'both passwords are different')
                return redirect('signup_page')
    
    form = RegisterForm()
    return render(request,'signup.html',{'form':form})
 

def logout_view(request):
    logout(request)
    return redirect('dashboard')

@login_required
def create_profile(request):  
    profile, created = Profile.objects.get_or_create(user=request.user)  
    if request.method == 'POST':
        u_form = userupdate(request.POST,instance=request.user)
        p_form = profileupdate(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            profile = p_form.save(commit=False)
            profile.user = request.user
            profile.save()
            u_form.save()
        messages.success(request,f'your profile has been updated')
        return redirect('profile_page')
    else:
        u_form = userupdate(instance=request.user)
        p_form = profileupdate(instance=request.user.profile)
        context = {'u_form':u_form,'p_form':p_form}
        return render(request,'profile.html',context)
@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('profile-page')
    
    if request.method == 'POST':
        u_form = userupdate(request.POST,instance=request.user)
        p_form = profileupdate(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request,f'your profile has been updated')
        return redirect('profile_page')
    else:
        u_form = userupdate(instance=request.user)
        p_form = profileupdate(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'editprofile.html', context)
    



        


#def signup_view(request):
 #   if(request.method == "POST"):
  #      usern = request.POST.get('username')
   ###     pass1 = request.POST.get('password1')
  #      mail = request.POST.get('email')
  #      pass2 = request.POST.get('password2')
  #      if(pass1 != pass2):
  #          d ={}
  #          ans = "Both passwords should be same"
  #          d = {'pas':ans}
  #          return render(request,'signup.html',d)
   #     else:
   #         my_user = User.objects.create_user(usern,pass1,mail)
   #         my_user.save()
   #         return redirect('/')
        
   # return render(request,'signup.html')
def dash(request):
    news = News.objects.all()
    context = {'news':news}
    return render(request,'dashboard.html',context)

def about(request):
    return render(request,'about.html')

def course(request):
    courses = cours.objects.all()
    return render(request,'courses.html',{'course':courses})
def contact(request):
    return render(request,'contact.html')

@login_required
def todo_list(request):
    co = cours.objects.all()
    todo_tasks = todo.objects.filter(user = request.user)
    coursename = []
    if(request.method =='POST'):
        form = cheetah(request.POST)
        if(form.is_valid()):
            selected_course = form.cleaned_data['course_field']
            coursename = cours.objects.filter(course_field = selected_course)

    else:
        form = cheetah()  


    context = {'form':form,'coursename':coursename,'task':todo_tasks}    
    #return render(request,'todolist.html',{'form':form,'coursename':coursename})
    return render(request,'todolist.html',context)
@login_required
def add_task(request,course_id):
    task = get_object_or_404(cours,id = course_id)
    todo_task, created = todo.objects.get_or_create(user = request.user,work = task)
    todo_task.save()
    return redirect('todolist')

def course_detail(request,course_id):
    course1 = get_object_or_404(cours,pk=course_id)
    course = cours.objects.all()
    
    return render(request,'course_detail.html',{'course1':course1,'course':course})
l = []

@login_required
def addcourse(request,course_id):
    addc = cours.objects.get(id = course_id)
    ans = " "
    if(request.method == 'POST'):
        add = addForm(request.POST,instance=addc)
        if(add.is_valid):
            add.save()
            if(addc not in l):
                l.append(addc)
            else:
                ans = " already enrolled"
            context = {'add':add,'ans':ans}
            return render(request,'todolist.html',context)
    else:
        add = addForm(instance=addc)
    return render(request,'courseadd.html',{'add':add})



    
    


