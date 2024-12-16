from django import forms
from .models import *
from mychat.models import ChatGroup

class Postform(forms.ModelForm):

     class Meta:
        model = post
        fields = ['post_pic','caption']

class Commentform(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['text']

class chatForm(forms.ModelForm):

    class Meta:
        model = messaging
        fields = ['msg']


class ChatGroupForm(forms.Form):
    Group_name = forms.CharField(max_length=250)
    members = forms.ModelMultipleChoiceField(queryset = Profile.objects.all(),widget=forms.CheckboxSelectMultiple)
    



    
