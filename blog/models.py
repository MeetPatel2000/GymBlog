from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    retype_password = models.CharField(max_length=255, default='')
    data_registered = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return self.username
    
