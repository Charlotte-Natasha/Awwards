from django import forms
from django.contrib.auth.models import User
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:  
        model = Profile
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__' 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'design', 'usability', 'content']           