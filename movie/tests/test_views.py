from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from movie.models import Movie
from movie.views import MovieDetail

class TestMovieListViews(APITestCase):
    url = reverse('movie-list')
    def setUp(self):
        self.movie = Movie.objects.create(
            title = 'As longas tranças de um careca',
            genre = 'Thriller',
            length = 90
        )

    def test_movie_list_post(self):
        '''
        Testing the post request: it shall return the status code 201
        because all the data being send is valid, and the number of movie
        objects must be two, because the setUp method creates one when
        this test is run
        '''
        data = {
            'title': 'Poeira em Alto Mar',
            'genre': 'Comédia',
            'length': 92
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        
    def test_movie_list_post_error(self):
        '''
        Testing the post request: it shall return the status code 400
        because the data being send isn't valid(the title field is
        required), and there must be only one object (the one created
        in the setUp method)
        '''
        data = {
            'genre': 'Comédia',
            'length': 92
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Movie.objects.count(), 1)
    
    def test_movie_list_get(self):
        '''
        Testing the get request: it shall return the status code 200
        and the number of Movie objects must be equal to one because
        there is only one object in the database used for testing
        '''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Movie.objects.count(), 1)

class TestMovieDetailViews(APITestCase):
    url = reverse('movie-detail', kwargs={'pk':1})
    def setUp(self):
        self.movie = Movie.objects.create(
            title = 'As longas tranças de um careca',
            genre = 'Thriller',
            length = 90
        )
    
    movie_put = Movie.objects.filter().first()
    def test_movie_detail_put(self):
        '''
        Testing the put request: it shall return the status code 200
        once that all the data sent is valid, also the first movie
        object of the database should have it's length value equal to
        95, the value sent by the request
        '''
        data = {
            'title': 'As longas tranças de um careca',
            'genre': 'Thriller',
            'length': 95
        }

        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.movie_put.length, 95)

    def test_movie_detail_put_error(self):
        '''
        Testing the put request: it shall return the status code 400
        because the data sent is invalid(required value doesn't exist),
        and the length value of the first movie object in the testing
        database should be equal to 90 (the value defined in the setUp
        method), because the new value failed to be send
        '''
        data = {
            'genre': 'Comédia',
            'length': 95
        }

        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(self.movie_put.length, 95)

    def test_movie_detail_delete(self):
        '''
        Testing the delete request: the request shall return the status
        code 204 because it was successful at deleting the wanted object,
        also when searching if the deleted object exists in the database
        it must return false
        '''
        response = self.client.delete(self.url)
        movie = Movie.objects.filter(pk=1).exists()
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(movie)
    
    def test_movie_detail_delete_erro(self):
        '''
        Testing the delete request: the request shall return the status
        code 404 once that the object with the given primary key doesn't
        exist in the database, also the count of movie objects must be
        equal to one(the one created in the setUp method)
        '''
        url_deletar_erro = reverse('movie-detail', kwargs={'pk':2})
        response = self.client.delete(url_deletar_erro)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Movie.objects.count(), 1)