
import imp
from unicodedata import name
from django import views
from django.urls import path
from hospital import views
urlpatterns = [
    path('',views.home, name='home'),
    
]
