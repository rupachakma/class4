
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("hello world")
    
def service(request):
    return HttpResponse("<h1>Welcome to Service page</h1>")
def soft(request):
    return HttpResponse("soft service")

def hello(request):
    return HttpResponse("hello world")

def kitty(request):
    return HttpResponse("wellcome to kitty world")

