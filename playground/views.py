from django.shortcuts import render
from django.http import HttpRequest

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    name = "Husnoro"
    x = calculate()
    return render(request, 'hello.html', {'name': 'Husnoro'})
