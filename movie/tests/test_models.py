from django.test import TestCase
from movie.models import Movie

class TestModelMovie(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title = 'As longas tranças de um careca',
            genre = 'Thriller',
            length = 90
        )
    
    def test_movie_setup(self):
        self.movie = Movie.objects.all()[0]
        self.assertEqual(self.movie.title, 'As longas tranças de um careca')

    def test_movie_setup_wrong(self):
        self.movie = Movie.objects.all()[0]
        self.assertNotEqual(self.movie.title, 'As curtas tranças de um careca')
