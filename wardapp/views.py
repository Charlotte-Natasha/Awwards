from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'wardapp/index.html')

def sign_up(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES['image']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(author=user, profile_picture=image)
        user.save()
        profile.save()

        if profile:
            messages.success(request,'Profile Created Please Login')
            return redirect('login')

    else:  
        return render(request, 'registration/signup.html', {})      

def profile(request):
    return render(request, 'wardapp/profile.html', {})

def editprofile(request):
    if request.method == 'POST':
        # logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'wardapp/editprofile.html', {})  

def project(request):
    return render(request, 'wardapp/project.html')      
