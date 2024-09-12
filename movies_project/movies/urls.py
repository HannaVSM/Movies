from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('c-movie/', views.createMovie),
    path('er-movie/<int:id>', views.editionMovie),
    path('e-movie/<int:id>', views.editMovie),
    path('d-movie/<int:id>', views.deleteMovie),
    path('search/',views.searchMovies),
    path('i-search/',views.searchMoviesI),
    path('top/', views.topMovies),
    path('summary/', views.summaryMovies)
]