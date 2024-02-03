from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world")


def hello_from_django(request, name):
    return HttpResponse(f"Hello from: Django! {name}")
