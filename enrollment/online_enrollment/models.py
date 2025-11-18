from django.db import models

class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

# Commented out to avoid RuntimeError
class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"
    
class Student(models.Model):
    student_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_id}"
    
class Course(models.Model):
    course_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.course_id}"  

class Payment(models.Model):
    student_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=100)  
    payment_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_id}"
    
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    instructor_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
    
class Enrollment(models.Model):
    enrollment_id = models.CharField(max_length=20)
    course_id = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    enrollment_date = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.enrollment_id}"




