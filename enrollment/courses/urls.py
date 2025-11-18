from django.urls import path
from . import views

urlpatterns =[
    path('courses/', views.courses, name = "courses"),
    path('bssw/', views.bssw, name = "Bachelor of Science in Social Work"),
    path('bsit/', views.bsit, name = "Bachelor of Science in Information Technology"),
    path('bssw/', views.bse, name = "Bachelor of Science in Entrepreneurship"),
]