from django import forms
from django.contrib.auth.models import User
from LearningUsers.models import UserProfileInfoClass

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoClassForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfoClass
        fields=('portfolio_site','profile_pic')
