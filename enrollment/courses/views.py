from django.shortcuts import render
from django.http import HttpResponse


def courses (request):
    return HttpResponse ("This is the Courses")

def bssw (request):
    return HttpResponse ("BSSW")

def bsit (request):
    return HttpResponse ("BSIT")

def bse (request):
    return HttpResponse ("BSE")

# Create your views here.
