from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='xlapp'),
    path('create/', CreateMovieView.as_view(), name='create'),
    path('update/', UpdateMovieView.as_view(), name='update')
]