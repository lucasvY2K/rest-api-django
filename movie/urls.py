from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movie import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie-list'),
    path('<int:pk>', views.MovieDetail.as_view(), name='movie-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)