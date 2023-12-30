from django.urls import path
from . import views

urlpatterns = [
    path('myweb', views.mywebapp, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
]
