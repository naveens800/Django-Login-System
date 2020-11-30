from django.db.models import fields
from .models import UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields=['username','password','email','first_name']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['department','profile_pic']