from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,"index.html",context={})

def shopping_cart(request):
    return HttpResponse("This is the shopping cart page")