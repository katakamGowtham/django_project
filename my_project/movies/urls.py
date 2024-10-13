
from django.urls import path # type: ignore
from .views import movie_list,movie_detail,add_movie,edit_movie,delete_movie,register # Importing the movie_list view

urlpatterns = [
    path('', movie_list, name='movie_list'),  # Maps the root URL of movies to the movie_list view
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('add/', add_movie, name='add_movie'), # type: ignore
    path('movie/edit/<int:movie_id>/', edit_movie, name='edit_movie'), # type: ignore
    path('movie/delete/<int:movie_id>/', delete_movie, name='delete_movie'),   # type: ignore
    path('register/', register, name='register'),  # Add this line
]
