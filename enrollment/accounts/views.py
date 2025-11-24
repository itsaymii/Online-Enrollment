from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TailwindAuthenticationForm, StudentForm, CourseForm, PaymentForm, InstructorForm, EnrollmentForm


from django.views.decorators.csrf import csrf_exempt
@login_required
@csrf_exempt
def enrollments_list(request):
    enrollments = Enrollment.objects.all()
    add_form = EnrollmentForm()
    enrollment_forms = [(e, EnrollmentForm(instance=e)) for e in enrollments]

    # Handle Add Enrollment
    if request.method == 'POST' and request.POST.get('action') == 'add':
        add_form = EnrollmentForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'Enrollment added successfully!')
            return redirect('enrollments_list')

    # Handle Edit Enrollment
    if request.method == 'POST' and request.POST.get('action', '').startswith('edit_'):
        enrollment_id = request.POST.get('enrollment_id')
        for idx, (enrollment, form) in enumerate(enrollment_forms):
            if str(enrollment.enrollment_id) == str(enrollment_id):
                edit_form = EnrollmentForm(request.POST, instance=enrollment)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Enrollment updated successfully!')
                    return redirect('enrollments_list')
                enrollment_forms[idx] = (enrollment, edit_form)

    return render(request, 'accounts/enrollments_list.html', {
        'enrollments': enrollments,
        'enrollment_forms': enrollment_forms,
        'add_form': add_form,
    })


from django.views.decorators.csrf import csrf_exempt
@login_required
@csrf_exempt
def instructors_list(request):
    instructors = Instructor.objects.all()
    add_form = InstructorForm()
    instructor_forms = [(i, InstructorForm(instance=i)) for i in instructors]

    # Handle Add Instructor
    if request.method == 'POST' and request.POST.get('action') == 'add':
        add_form = InstructorForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'Instructor added successfully!')
            return redirect('instructors_list')

    # Handle Edit Instructor
    if request.method == 'POST' and request.POST.get('action', '').startswith('edit_'):
        instructor_id = request.POST.get('instructor_id')
        for idx, (instructor, form) in enumerate(instructor_forms):
            if str(instructor.instructor_id) == str(instructor_id):
                edit_form = InstructorForm(request.POST, instance=instructor)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Instructor updated successfully!')
                    return redirect('instructors_list')
                instructor_forms[idx] = (instructor, edit_form)

    return render(request, 'accounts/instructors_list.html', {
        'instructors': instructors,
        'instructor_forms': instructor_forms,
        'add_form': add_form,
    })


from django.views.decorators.csrf import csrf_exempt
@login_required
@csrf_exempt
def payments_list(request):
    payments = Payment.objects.all()
    add_form = PaymentForm()
    payment_forms = [(p, PaymentForm(instance=p)) for p in payments]

    # Handle Add Payment
    if request.method == 'POST' and request.POST.get('action') == 'add':
        add_form = PaymentForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'Payment added successfully!')
            return redirect('payments_list')

    # Handle Edit Payment
    if request.method == 'POST' and request.POST.get('action', '').startswith('edit_'):
        payment_id = request.POST.get('payment_id')
        for idx, (payment, form) in enumerate(payment_forms):
            if str(payment.payment_id) == str(payment_id):
                edit_form = PaymentForm(request.POST, instance=payment)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Payment updated successfully!')
                    return redirect('payments_list')
                payment_forms[idx] = (payment, edit_form)

    return render(request, 'accounts/payments_list.html', {
        'payments': payments,
        'payment_forms': payment_forms,
        'add_form': add_form,
    })

def courses_list(request):
    courses = Course.objects.all()
    add_form = CourseForm()
    course_forms = [(c, CourseForm(instance=c)) for c in courses]

    # Handle Add Course
    if request.method == 'POST' and request.POST.get('action') == 'add':
        add_form = CourseForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('courses_list')

    # Handle Edit Course
    if request.method == 'POST' and request.POST.get('action', '').startswith('edit_'):
        course_id = request.POST.get('course_id')
        for idx, (course, form) in enumerate(course_forms):
            if str(course.course_id) == str(course_id):
                edit_form = CourseForm(request.POST, instance=course)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Course updated successfully!')
                    return redirect('courses_list')
                course_forms[idx] = (course, edit_form)

    return render(request, 'accounts/courses_list.html', {
        'courses': courses,
        'course_forms': course_forms,
        'add_form': add_form,
    })

from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

from online_enrollment.models import Student, Course, Payment, Instructor, Enrollment
from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt
@login_required
@csrf_exempt
def students_list(request):
    students = Student.objects.all()
    add_form = StudentForm()
    student_forms = [(s, StudentForm(instance=s)) for s in students]

    if request.method == 'POST' and request.POST.get('action') == 'add':
        add_form = StudentForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'Student added successfully!')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                students = Student.objects.all()
                student_forms = [(s, StudentForm(instance=s)) for s in students]
                from django.template.loader import render_to_string
                html = render_to_string('accounts/student_table_fragment.html', {
                    'students': students,
                    'student_forms': student_forms,
                }, request=request)
                return JsonResponse({'success': True, 'html': html})
            return redirect('students_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                from django.template.loader import render_to_string
                error_html = render_to_string('accounts/add_student_form_errors.html', {
                    'add_form': add_form,
                }, request=request)
                return JsonResponse({'success': False, 'errors': error_html})

    # Handle Edit Student
    if request.method == 'POST' and request.POST.get('action', '').startswith('edit_'):
        student_id = request.POST.get('student_id')
        for idx, (student, form) in enumerate(student_forms):
            if str(student.student_id) == str(student_id):
                edit_form = StudentForm(request.POST, instance=student)
                if edit_form.is_valid():
                    edit_form.save()
                    return redirect('students_list')
                student_forms[idx] = (student, edit_form)

    return render(request, 'accounts/students_list.html', {
        'students': students,
        'student_forms': student_forms,
        'add_form': add_form,
    })

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login_user')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = TailwindAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid input.')
    else:
        form = TailwindAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_user')



@login_required
def dashboard(request):
    tab = request.GET.get('tab', 'students')
    context = {'tab': tab}

    # Handle POST for all tabs
    if request.method == 'POST':
        action = request.POST.get('action', '')
        # Students
        if tab == 'students':
            if action == 'add':
                add_form = StudentForm(request.POST)
                if add_form.is_valid():
                    add_form.save()
                    messages.success(request, 'Student added successfully!')
                    return redirect(f'{request.path}?tab=students')
                context['add_form'] = add_form
            elif action.startswith('edit_'):
                student_id = request.POST.get('student_id')
                student = Student.objects.get(student_id=student_id)
                edit_form = StudentForm(request.POST, instance=student)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Student updated successfully!')
                    return redirect(f'{request.path}?tab=students')
                # fallback: show errors in modal
                context['edit_form'] = edit_form
        # Courses
        elif tab == 'courses':
            if action == 'add':
                add_form = CourseForm(request.POST)
                if add_form.is_valid():
                    add_form.save()
                    messages.success(request, 'Course added successfully!')
                    return redirect(f'{request.path}?tab=courses')
                context['add_form'] = add_form
            elif action.startswith('edit_'):
                course_id = request.POST.get('course_id')
                course = Course.objects.get(course_id=course_id)
                edit_form = CourseForm(request.POST, instance=course)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Course updated successfully!')
                    return redirect(f'{request.path}?tab=courses')
                context['edit_form'] = edit_form
        # Payments
        elif tab == 'payments':
            if action == 'add':
                add_form = PaymentForm(request.POST)
                if add_form.is_valid():
                    add_form.save()
                    messages.success(request, 'Payment added successfully!')
                    return redirect(f'{request.path}?tab=payments')
                context['add_form'] = add_form
            elif action.startswith('edit_'):
                payment_id = request.POST.get('payment_id')
                payment = Payment.objects.get(payment_id=payment_id)
                edit_form = PaymentForm(request.POST, instance=payment)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Payment updated successfully!')
                    return redirect(f'{request.path}?tab=payments')
                context['edit_form'] = edit_form
        # Instructors
        elif tab == 'instructors':
            if action == 'add':
                add_form = InstructorForm(request.POST)
                if add_form.is_valid():
                    add_form.save()
                    messages.success(request, 'Instructor added successfully!')
                    return redirect(f'{request.path}?tab=instructors')
                context['add_form'] = add_form
            elif action.startswith('edit_'):
                instructor_id = request.POST.get('instructor_id')
                instructor = Instructor.objects.get(instructor_id=instructor_id)
                edit_form = InstructorForm(request.POST, instance=instructor)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Instructor updated successfully!')
                    return redirect(f'{request.path}?tab=instructors')
                context['edit_form'] = edit_form
        # Enrollments
        elif tab == 'enrollments':
            if action == 'add':
                add_form = EnrollmentForm(request.POST)
                if add_form.is_valid():
                    add_form.save()
                    messages.success(request, 'Enrollment added successfully!')
                    return redirect(f'{request.path}?tab=enrollments')
                context['add_form'] = add_form
            elif action.startswith('edit_'):
                enrollment_id = request.POST.get('enrollment_id')
                enrollment = Enrollment.objects.get(enrollment_id=enrollment_id)
                edit_form = EnrollmentForm(request.POST, instance=enrollment)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request, 'Enrollment updated successfully!')
                    return redirect(f'{request.path}?tab=enrollments')
                context['edit_form'] = edit_form

    # Always provide fresh data for the selected tab
    if tab == 'students':
        context['students'] = Student.objects.all()
        context['add_form'] = context.get('add_form', StudentForm())
        context['student_forms'] = [(s, StudentForm(instance=s)) for s in context['students']]
    elif tab == 'courses':
        context['courses'] = Course.objects.all()
        context['add_form'] = context.get('add_form', CourseForm())
        context['course_forms'] = [(c, CourseForm(instance=c)) for c in context['courses']]
    elif tab == 'payments':
        context['payments'] = Payment.objects.all()
        context['add_form'] = context.get('add_form', PaymentForm())
        context['payment_forms'] = [(p, PaymentForm(instance=p)) for p in context['payments']]
    elif tab == 'instructors':
        context['instructors'] = Instructor.objects.all()
        context['add_form'] = context.get('add_form', InstructorForm())
        context['instructor_forms'] = [(i, InstructorForm(instance=i)) for i in context['instructors']]
    elif tab == 'enrollments':
        context['enrollments'] = Enrollment.objects.all()
        context['add_form'] = context.get('add_form', EnrollmentForm())
        context['enrollment_forms'] = [(e, EnrollmentForm(instance=e)) for e in context['enrollments']]

    from django.contrib import messages as msg_framework
    context['messages'] = msg_framework.get_messages(request)
    return render(request, 'accounts/dashboard.html', context)