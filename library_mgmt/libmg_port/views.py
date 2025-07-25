from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.


def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def shopping_cart(request):
    return HttpResponse("This is the shopping cart page")

def save_student(request):
    student_name = request.POST['student_name']
    return render(request, "welcome.html", context={'student_name': student_name})