from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100,default="",blank=True)
    last_name = models.CharField(max_length=100,default="",blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10,default="" ,choices=[('male', 'Male'), ('female', 'Female'), ('not_say', 'Prefer not to say')])
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    data_registered = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
