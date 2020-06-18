from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

# Create your views here.
def listMovie(request):
    movies = Movie.objects.all().order_by('-score')
    context = {
        'movies': movies
    }
    return render(request, 'movies/list.html', context)

def info(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/info.html', context)

def create(request):
    if request.method == "POST" :
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:list')
    else :
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request, 'movies/create.html', context)

def delete(request, pk) :
    Movie.objects.get(pk=pk).delete()
    return redirect('movies:list')

def edit(request, pk) :
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST" :
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:info', movie.pk)
    else :
        form = MovieForm(instance=movie)
    context = {
        'form' : form
    }
    return render(request, 'movies/edit.html', context)