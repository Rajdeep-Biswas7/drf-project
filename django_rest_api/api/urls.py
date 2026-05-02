from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.student_detail),
    path('students/<int:pk>/update/', views.student_update),
    path('students/<int:pk>/delete/', views.student_delete),    
]