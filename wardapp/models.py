from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField( upload_to='profilepics')
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def save_profile(self):
        self.author

    def delete_profile(self):
        self.delete()    

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(author__username__icontains=name).all()
