from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, 'secondapp/index.html')

def static_example(request) :
    return render(request, 'secondapp/static_example.html')