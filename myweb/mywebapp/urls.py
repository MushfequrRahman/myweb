from django.urls import path
from . import views

urlpatterns = [
    path('', views.mywebapp, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
]
