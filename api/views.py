from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_movies': '/',
        'Search by Genre': '/?genre=genre_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/movie/pk/delete'
    }

    return Response(api_urls)

@api_view(['POST'])
def add_movies(request):
    movie = MovieSerializer(data = request.data)

    if Movie.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if movie.is_valid():
        movie.save()
        return Response(movie.data)
    else:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_movies(request):
    if request.query_params:
        movies = Movie.objects.filter(**request.query_params.dict())
    else:
        movies = Movie.objects.all()
    
    if movies:
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def update_movies(request, pk):
    movie = Movie.objects.all()
    data = MovieSerializer(instance=movie, data = request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_movies(request, pk):
    movie = get_object_or_404(Movie, pk = pk)
    movie.delete()
    return Response(status = status.HTTP_202_ACCEPTED)