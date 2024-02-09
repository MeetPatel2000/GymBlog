from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('homepage/',views.homepage,name='homepage'),
    path('blog/',views.blog,name='blog'),
]