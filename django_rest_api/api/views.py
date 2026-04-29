from django.shortcuts import render
from django.http import JsonResponse
def StudentList(request):
    students=[
        {'id':1,'name':'John Doe','age':20},
        {'id':2,'name':'Jane Doe','age':22},
        {'id':3,'name':'Jim Doe','age':21},
    ]
    return JsonResponse(students, safe=False)  
# Create your views here.
