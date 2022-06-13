from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('addproject', views.addproject, name='addproject'),
    # path('review<id>/', views.review, name='review'),
    path('api/profile',views.ProfileList.as_view(), name='profile'),
    path('api/projects',views.ProjectList.as_view(), name='projects'),
    path('comment/<id>', views.comment, name='comment'),
]
