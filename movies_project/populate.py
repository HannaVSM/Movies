import os
import django

# Configuración del entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies_project.settings")
django.setup()

from movies.models import Movie

def populate():
    movies = [
        {"title": "Jojo Rabbit", "country": "USA", "rating": 8.8},
        {"title": "The House That Jack Built", "country": "Dinamarca", "rating": 8.6},
        {"title": "Howl no Ugoku Shiro", "country": "Japan", "rating": 8.6},
        {"title": "(500) Days of Summer", "country": "USA", "rating": 8.7},
        # Añade más películas aquí si lo deseas
    ]

    for movie_data in movies:
        movie, created = Movie.objects.get_or_create(
            title=movie_data['title'],
            defaults={
                'country': movie_data['country'],
                'rating': movie_data['rating'],
            }
        )
        if created:
            print(f"Película creada: {movie.title}")
        else:
            print(f"Película ya existente: {movie.title}")

if __name__ == "__main__":
    populate()
