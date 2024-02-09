from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
import random
import string

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
            # Generate a 6-character verification code
            verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            request.session['verification_code'] = verification_code
            
            UserProfile.objects.create(
                username=username,
                email=email,
                password=password,
                retype_password=retype_password
            )
            
             # Send verification email
            subject = 'Verify Your Account'
            message = f'Your verification code is: {verification_code}'
            from_email = 'darorak12@gmail.com'
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)
            
            return redirect('signup')
        else:
            error_message = 'Passwords do not match.'
            js_script = 'alert("Passwords do not match!");'
            return render(request, 'homepage.html', {'error_message': error_message, 'js_script': js_script})
    else:
         return render(request, 'homepage.html')

def signup(request):
    
    if request.method == "POST":
        stored_verification_code = request.session.get('verification_code', None)
        user_enterd_code = ''.join(request.POST.get(f'verification_code_{i}','') for i in range(1,7))
        if stored_verification_code:
            
            if user_enterd_code == stored_verification_code:
                # First Clear the code from session
                request.session.pop('verification_code',None)
                messages.success(request,'Signup Successful!')
                return redirect('blog')
            else:
                messages.error(request,'Verification code does not match. Please try again')
                return render(request,'signup.html')
        else:
            messages.error(request,'Verification code not found. Please go back to homepage and try again')
    
    return render(request,'signup.html')

def blog(request):
    return render(request,'blog.html')