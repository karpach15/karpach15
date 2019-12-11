from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	path('', views.account_profile, name="account_profile"),
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
	path('logout/', views.logout, name="logout")
]