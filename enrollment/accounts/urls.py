from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('students/', views.students_list, name='students_list'),
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/edit/<str:course_id>/', views.edit_course, name='edit_course'),
    path('payments/', views.payments_list, name='payments_list'),
    path('instructors/', views.instructors_list, name='instructors_list'),
    path('enrollments/', views.enrollments_list, name='enrollments_list'),
]