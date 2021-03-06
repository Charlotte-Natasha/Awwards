from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def index(request):
    project = Project.objects.all()
    if request.method == 'POST':
        project_id = request.POST.get('project-id')
        project = Project.objects.filter(id=project_id).first()

        if project and project.user == request.user:
            project.delete() 
    return render(request, 'wardapp/index.html', {'project':project})

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(user=user, profile_picture=image, bio=bio)
        user.save()
        profile.save()

        if profile:
            messages.success(request,'Profile Created Please Login')
            return redirect('login')

    else:  
        return render(request, 'registration/signup.html', {})      

@login_required(login_url="/login")
def profile(request):
    user = request.user
    profile = Profile.objects.get( user = user)

    return render(request, 'wardapp/profile.html', {'profile':profile})

@login_required(login_url="/login")
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

@login_required(login_url="/login")
def addproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'wardapp/addproject.html', {'form':form})      

# def review(request, id):
#     project = Project.objects.get(id = id)
#     user = request.user

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             rate = form.save(commit=False)
#             rate.user = user
#             rate.projects = project
#             rate.save()
#             return redirect('home')
#     else:
#         form = ReviewForm()
#     return render(request, 'wardapp/review.html', {'form':form, 'project':project}) 

@login_required(login_url="/login")
def comment(request, id):
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
    return render(request, 'wardapp/comment.html', {'form':form, 'project':project})               


class ProfileList(APIView):
    def get(self,request,format = None):
        all_profile = Profile.objects.all()
        serializerdata = ProfileSerializer(all_profile,many = True)
        return Response(serializerdata.data)

class ProjectList(APIView):
    def get(self,request,format = None):
        all_projects = Project.objects.all()
        serializerdata = ProjectSerializer(all_projects,many = True)
        return Response(serializerdata.data)    