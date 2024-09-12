from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from django.db.models import Q
from django.db.models import Count, F, Func

def home (request):
    listMovies = Movie.objects.all()
    return render(request, "movies.html", {"movies": listMovies})

def createMovie (request):
    title = request.POST['txtTitle']
    country = request.POST['txtCountry']
    rating = request.POST['numRating']

    movie = Movie.objects.create(title=title, country=country, rating=rating)
    return redirect('/')

def editionMovie(request, id):
    movie = Movie.objects.get(id = id)
    return render(request, "editionMovie.html", {"movie": movie})


def editMovie(request,id):
    title = request.POST['txtTitle']
    country = request.POST['txtCountry']
    rating = request.POST['numRating']

    movie = Movie.objects.get(id=id)
    movie.title = title
    movie.country = country
    movie.rating = rating
    movie.save()

    return redirect('/')


def deleteMovie(request, id):
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')

from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from .models import Movie

def searchMovies(request):
    
    query = request.GET.get('q', '')
    sort_field = request.GET.get('s', 'title')
    order = request.GET.get('o', 'asc') 
    
    valid_sort_fields = {
        'nombre': 'title',        
        'pais': 'country',        
        'calificacion': 'rating'  
    }
    sort_field = valid_sort_fields.get(sort_field, 'title')

    if order == 'desc':
        sort_field = f'-{sort_field}'
    
   
    movies = Movie.objects.filter(
        Q(title__icontains=query) | Q(country__icontains=query)
    ).order_by(sort_field)
    
    movies_list = list(movies.values('id', 'title', 'country', 'rating'))
    return JsonResponse(movies_list, safe=False)

def searchMoviesI(request):
    query = request.GET.get('q', '')

    movies = Movie.objects.filter(
        Q(title_icontains=query) | Q(country_icontains=query)
    )
    movies_list = list(movies.values('id', 'title', 'country', 'rating'))
    return JsonResponse(movies_list, safe=False)

def topMovies(request):
    movies = Movie.objects.order_by('-rating')[:5]
    movies_list = list(movies.values('id', 'title', 'country', 'rating'))
    return JsonResponse(movies_list, safe=False)

# Función para redondear la calificación
class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'  # Redondear sin decimales

def summaryMovies(request):
   
    movies_by_country = Movie.objects.values('country').annotate(total=Count('id')).order_by('-total')

    
    movies_by_rating = Movie.objects.annotate(
        rounded_rating=Round(F('rating'))
    ).values('rounded_rating').annotate(total=Count('id')).order_by('rounded_rating')

    
    summary = {
        'movies_by_country': list(movies_by_country),
        'movies_by_rating': list(movies_by_rating)
    }

    return JsonResponse(summary, safe=False)