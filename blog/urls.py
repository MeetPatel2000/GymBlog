from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/',views.contact,name='contact'),
    path('email_verification/',views.email_verification,name='email_verification'),
    path('homepage/',views.homepage,name='homepage'),
    path('blog/',views.blog,name='blog'),
    path('login/',views.login_view,name='login_view'),
    path('register/',views.register,name='register'),
    path('logout_view', views.logout_view, name='logout_view'),
    # path('email_verification/<int:user_id>/', views.email_verification, name='email_verification'),
]