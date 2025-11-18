from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.student_details, name='student_details'),
    path("courses/", views.course_details, name='course_details'),
    path("payments/", views.payment_details, name='payment_details'),
    path("instructors/", views.instructor_details, name='instructor_details'),
    path("enrollments/", views.enrollment_details, name='enrollment_details'),
]