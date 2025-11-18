from django.shortcuts import render, redirect
from .models import Student, Payment, Instructor, Enrollment
from .forms import StudentForm


def student_details(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success.html')
    else:
        form = StudentForm()
    return render(request, 'student.html', {'students': students, 'form': form})

def course_details(request):
    courses = Course.objects.all() 
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success.html')
    else:
        form = CourseForm()
    return render(request, 'student/enroll.html', {'form': form})

def payment_details(request):
    payments = Payment.objects.all()
    return render(request, 'payment.html', {"payments": payments})

def instructor_details(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor.html', {"instructors": instructors})

def enrollement_details(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment.html', {"enrollments": enrollments})

