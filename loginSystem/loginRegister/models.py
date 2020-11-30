from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

# Create your models here.
class UserProfile(Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to ='profile_pics',blank = True)


    def __str__(self):
        return self.user.username
