from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'wardapp/index.html')

def sign_up(request):
    if request.method == 'POST':
    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # password1 = request.POST['password1']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')
    else:  
        return render(request, 'registration/signup.html', {})      