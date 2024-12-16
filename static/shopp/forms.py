from django import forms
from .models import *
from bunch.models import Profile

class searchForm(forms.ModelForm):
    
    class Meta:
        model = shopsy
        fields = ['item_name']

class address(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address']





