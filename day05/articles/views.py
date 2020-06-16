from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request) :
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    
    return render(request, 'articles/index.html', context)

def new_write(request) :
    return render(request, 'articles/new.html')

def create(request) :
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)
    
    return redirect('articles:index')

def introduce(request) :
    context = {
        'name' : '이영주', 
        'age' : '28'
    }
    return render(request, 'articles/introduce.html', context)

def detail(request, pk) :
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request, 'articles/detail.html', context)

def delete(request, pk) :
    # request.method
    
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')

def edit(request, pk) :
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk) :
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', pk)
