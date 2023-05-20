from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_movies, name='add-movies'),
    path('all/', views.view_movies, name='view-movies'),
    path('update/<int:pk>/', views.update_movies, name='update-movies'),
    path('movie/<int:pk>/delete', views.delete_movies, name='delete-movies'),
]