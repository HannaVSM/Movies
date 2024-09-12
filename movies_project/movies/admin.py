from django.contrib import admin
from .models import Movie

#Permite que el modelo aparezca en la interfaz de administración
admin.site.register(Movie)
