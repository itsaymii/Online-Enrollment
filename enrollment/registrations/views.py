from django.shortcuts import render
from django.http import HttpResponse


def register (request):
    return HttpResponse ("This is the Registration")

def contact (request):
    return HttpResponse ("Contact")

def payment (request):
    return HttpResponse ("Payment")

def grades (request):
    return HttpResponse ("Grades")

# Create your views here.
