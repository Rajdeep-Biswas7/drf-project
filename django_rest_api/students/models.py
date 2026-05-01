from django.db import models

class Student(models.Model):
    Student_id = models.CharField(max_length=10, primary_key=True)
    Student_name = models.CharField(max_length=50)
    Student_branch = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Student_name
    # Create your models here.
