from django.urls import path
from .views import hello_world, hello_from_django, index

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('hello/', hello_from_django, name='hello_from_django'),
    path('index/', index, name='index')
]
