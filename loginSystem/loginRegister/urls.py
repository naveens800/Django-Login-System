from django.urls import path
from . import views

app_name = 'loginRegister'


urlpatterns = [

    path('login', views.user_login, name='user_login'),
    path('register', views.user_register,  name='register'),
]
