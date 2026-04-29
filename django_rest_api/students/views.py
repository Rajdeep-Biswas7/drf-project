from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = ["Alice", "Bob", "Charlie"]
      
    return HttpResponse("Hello, students!")
# Create your views here.
