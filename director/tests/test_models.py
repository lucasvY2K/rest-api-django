import datetime
from django.test import TestCase
from director.models import Director

class TestModelDirector(TestCase):
    def setUp(self):
        self.director = Director.objects.create(
            name = 'Glauber Rocha',
            birth_date = datetime.date(1939, 3, 14),
            nationality = 'Brazilian'
        )

    def test_director_setup(self):
        self.director = Director.objects.all()[0]
        self.assertEqual(self.director.name, 'Glauber Rocha')

    def test_director_setup_wrong(self):
        self.director = Director.objects.all()[0]
        self.assertNotEqual(self.director.name, 'Glauber Silva')