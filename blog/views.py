from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages

def homepage(request):
    return render(request,'homepage.html')

def contact(request):
    return render(request,'contact.html')

def homepage(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password == retype_password:
            UserProfile.objects.create(
                username=username,
                email=email,
                password=password,
                retype_password=retype_password
            )
            return redirect('signup')
        else:
            error_message = 'Passwords do not match.'
            return render(request, 'homepage.html', {'error_message': error_message})
    else:
        return render(request, 'homepage.html')

def signup(request):
    return render(request,'signup.html')