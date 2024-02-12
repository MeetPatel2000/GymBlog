from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class UserProfile(models.Model):
    fullname = models.CharField(max_length=50,default="",blank=True)
    username = models.CharField(max_length=50, default="", blank=True, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10,default="" ,choices=[('male', 'Male'), ('female', 'Female'), ('not_say', 'Prefer not to say')])
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    data_registered = models.DateTimeField(default=timezone.now) 
    
    
    def __str__(self):
        return f"{self.username}"

    
