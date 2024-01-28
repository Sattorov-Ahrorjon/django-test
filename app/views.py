from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world")


def hello_from_django(request):
    return HttpResponse("Hello from: Django!")


def index(request):
    return HttpResponse("Index Page")


def invoice(request):
    return HttpResponse("Invoice Page")
