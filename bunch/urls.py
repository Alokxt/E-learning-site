from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name="login_page"),
    path('dash/',views.dash,name="dashboard"),
    path('sinup/',views.signup_view,name ="signup_page"),
    path('about/',views.about,name ="about-us"),
    path('courses/',views.course,name="courses"),
    path('contact-us/',views.contact,name="contact"),
    path('todo/',views.todo_list,name="todolist"),
    path('course-details/<int:course_id>/',views.course_detail,name="course_details"),
    path('course-add/<int:course_id>/',views.addcourse,name = "add-course"),
    path('logout/',views.logout_view,name= 'logout'),
    path('add-task/<int:course_id>/',views.add_task,name = "add-task"),
    path('profile/',views.create_profile,name= 'profile_page'),
    path('update_profile/',views.edit_profile,name= 'update_profile'),


]