from django.urls import path
from . import views

urlpatterns =[
    path('register/', views.register, name = "This is the Registration"),
    path('payment/', views.payment, name = "Payments"),
    path('grade/', views.grades, name = "Grade"),
]