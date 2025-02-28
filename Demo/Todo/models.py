from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username=models.CharField(max_length=20,null=False,blank=False)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)

    def set_password(self,raw_password):
        self.password=make_password(raw_password)

    def check_password(self,raw_password):
        self.password=check_password(raw_password,self.password)

    def __str__(self):
        return self.username
