from django.db import models
from django.core.validators import RegexValidator,EmailValidator
# Create your models here.
phone_validator = RegexValidator(r'^\d{10,12}$', "Enter a valid phone number.")

class Student(models.Model):  
    rollno = models.CharField(max_length=10, unique=True)  #
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    email = models.EmailField(unique=True,validators=[EmailValidator]) 
    phone_number = models.CharField(max_length=12,validators=[phone_validator])  
    img = models.ImageField(upload_to='student_images/', blank=True, null=True)  

    def __str__(self):
        return f"{self.rollno} - {self.name}"
