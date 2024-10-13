from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth import login # type: ignore
from django.shortcuts import render, redirect, get_object_or_404  # type: ignore # Import necessary functions
from .models import Movie  # Import the Movie model
from .forms import MovieForm  # Import the MovieForm #type:ignore

# View for listing all movies
def movie_list(request):
    movies = Movie.objects.all()  # Fetch all movies from the database
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Home view
def home(request):
    return render(request, 'home.html')  # This will render the home template

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# View for displaying movie details
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)  # Fetch the movie or raise 404
    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
# View for adding a new movie
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new movie to the database
            return redirect('movie_list')  # Redirect to the movie list page
    else:
        form = MovieForm()  # Create an empty form
    return render(request, 'movies/add_movie.html', {'form': form})

# View for editing an existing movie
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)  # Fetch the movie or raise 404
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)  # Bind form with the existing movie
        if form.is_valid():
            form.save()  # Save the updated movie
            return redirect('movie_detail', movie_id=movie.id)  # Redirect to the movie detail page
    else:
        form = MovieForm(instance=movie)  # Create a form with existing movie data
    return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})

# View for deleting a movie
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)  # Fetch the movie or raise 404
    if request.method == 'POST':
        movie.delete()  # Delete the movie from the database
        return redirect('movie_list')  # Redirect to the movie list page
    return render(request, 'movies/delete_movie.html', {'movie': movie})



