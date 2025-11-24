from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.login_user, name='home'),


    path('', lambda request: redirect('login_user'), name='home'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]