from django import forms
from .models import *

class GroupChatMessage(forms.ModelForm):
    class Meta:
        model = Groupmessage
        fields =['body']
        widgets={
            'body':forms.TextInput(attrs={'placeholder':'Add message...','class':'p-4 text-black','maxlength':'300','autofocus':True}),
        }



