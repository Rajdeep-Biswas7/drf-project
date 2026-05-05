from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.emp_name    
# Create your models here.
