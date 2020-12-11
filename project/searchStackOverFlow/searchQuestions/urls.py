from django.urls import path,include
from . import views

app_name    = 'searchQuestions'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('queryForm/',views.handleQueryForm,name="index"),
    path('results/',views.paginateResults,name="results"),
]