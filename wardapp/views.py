from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    project = Project.objects.all()
    return render(request, 'wardapp/index.html', {'project':project})

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(user=user, profile_picture=image)
        user.save()
        profile.save()

        if profile:
            messages.success(request,'Profile Created Please Login')
            return redirect('login')

    else:  
        return render(request, 'registration/signup.html', {})      

def profile(request):
    # prof = Profile.objects.get()
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
    return render(request, 'wardapp/editprofile.html', {'form':form})  

def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            # user_image = form.save(commit=False)
            # user_image.user = current_user
            # user_image.save()
            form.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'wardapp/project.html', {'form':form})      

def review(request, id):
    project = Project.objects.get(id = id)
    user = request.user

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'wardapp/review.html', {'form':form, 'project':project})            