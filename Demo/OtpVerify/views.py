from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.

def Home(request):
    return render(request,"home.html")  

def create(request):
    return render(request,"create.html")


def registration(request):
    if request.method=="POST":
        RollNo=request.POST.get('rollno')
        Name=request.POST.get('name')
        Branch=request.POST.get('branch')
        Email=request.POST.get('email')
        Phone_Number=request.POST.get('phone_number')
        Image=request.POST.get('img')
        student=Student (
            rollno=RollNo,
            name=Name,
            branch=Branch,
            email=Email,
            phone_number=Phone_Number,
            img=Image
        )
        student.save()
        return redirect ("/view/")
    return render(request,'create.html')