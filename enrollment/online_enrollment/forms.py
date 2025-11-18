from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model =  Student
        fields = ['student_id', 'first_name', 'last_name', 'email', 'contact_number']
        widgets = {
            'student_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your student id'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'          
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your contact number'
            }),
        }        

# class CourseForm(forms.ModelForm):
#     class Meta:
#         model =  Course
#         fields = ['course id', 'course name', 'description', 'instructor', 'credits']

