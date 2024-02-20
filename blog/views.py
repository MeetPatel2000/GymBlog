from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.conf import settings
import random
import string

def homepage(request):
    return render(request,'homepage.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request,'blog.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me') == 'on'
        
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            login(request, user)
            if remember_me:
                response = redirect('blog')
                response.set_cookie('remembered_username', username, max_age=3600*24*30)  # Set the cookie to expire in 30 days
                response.set_cookie('remembered_password', password, max_age=3600*24*30)
                return response

            # Mark the session as modified
            request.session.modified = True
            
            return redirect('blog')
            
        else:
            messages.error(request, "Bad Credentials!!")    
        
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST.get('phone_number', '')  # Optional field
        password = request.POST['password']
        gender = request.POST['gender']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('register')
            
        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered. Try another email.')
            return redirect('register')

        # Generate a 6-character verification code
        verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        request.session['verification_code'] = verification_code

        # Send email with verification code
        send_mail(
            'Email Verification',
            f'Your verification code is: {verification_code}',
            'darorak12@gmail.com',  # Replace with your email address
            [email],
            fail_silently=False,
        )
        
        request.session['preliminary_user'] = {
            'fullname':fullname,
            'username':username,
            'email': email,
            'password': password,
            'gender': gender,
            'phone_number':phone_number,
            'verification_code': verification_code,
        }

        # Redirect to the email verification page
        return redirect('email_verification')

    return render(request, 'register.html')


def email_verification(request):
    if request.method == "POST":
        # Retrieve the preliminary user info from session
        preliminary_user = request.session.get('preliminary_user')

        if not preliminary_user:
            messages.error(request, 'Invalid session data. Please go back to homepage and try again.')
            return render(request, 'email_verification.html')

        user_entered_code = ''.join(request.POST.get(f'verification_code_{i}', '') for i in range(1, 7))
        
        username = preliminary_user['username']
        # Your existing verification logic
        if user_entered_code == preliminary_user['verification_code']:
            # Create the UserProfile and remove the verification code
            UserProfile.objects.create(
                fullname = preliminary_user['fullname'],
                username = preliminary_user['username'],
                email=preliminary_user['email'],
                password=preliminary_user['password'],
                gender=preliminary_user['gender'],
                phone_number = preliminary_user['phone_number']
                # Add other fields as needed
            )
            
            myuser = User.objects.create_user(
                username=preliminary_user['username'],
                email=preliminary_user['email'],
                password=preliminary_user['password'],
            )
            myuser.username = username
            myuser.is_active = True
            myuser.save()
            

            # Clear the session data
            request.session.pop('preliminary_user', None)

            messages.success(request, 'Signup Successful!')
            return redirect('blog')  # Change 'blog' to your desired URL after successful verification
        else:
            messages.error(request, 'Verification code does not match. Please try again.')
            return render(request, 'email_verification.html')

    return render(request, 'email_verification.html')

def logout_view(request):
    logout(request)
    return render(request,'homepage.html')
    
