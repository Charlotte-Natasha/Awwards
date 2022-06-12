from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profilepics')
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    projecturl= models.URLField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    


    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()