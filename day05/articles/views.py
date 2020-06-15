from django.shortcuts import render

# Create your views here.

def index(request) :
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content
    }
    
    return render(request, 'articles/index.html', context)

def new_write(request) :
    return render(request, 'articles/new.html')

def create(request) :
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content
    }
    
    return render(request, 'articles/create.html', context)

def introduce(request) :
    context = {
        'name' : '이영주', 
        'age' : '28'
    }
    return render(request, 'articles/introduce.html', context)