from django.contrib import admin
from . models import TestingDatabase, Student, Course, Payment, Instructor, Enrollment

admin.site.register(TestingDatabase)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'contact_number')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'description', 'instructor', 'credits')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'amount', 'payment_date', 'payment_method', 'payment_id')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'contact_number', 'instructor_id')

@admin.register(Enrollment)
class EnrollementAdmin(admin.ModelAdmin):
    list_display = ('enrollment_id', 'course_id', 'student_id', 'enrollment_date', 'status')