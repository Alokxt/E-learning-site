from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class cheetah(forms.ModelForm):
    course_field = forms.ChoiceField(choices= cours.choice,label= "select course field")
    

    class Meta:
        model = cours
        fields = ['course_field']

class addForm(forms.ModelForm):
    class Meta:
        model = cours
        fields = ['course_name']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class userupdate(forms.ModelForm):
    email = forms.EmailField()
    class  Meta:
        model = User
        fields = ['username','email']

class profileupdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']


    

    

    
