from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    return HttpResponse
    ("<h2>hola primera vista</h2>")

def display(request):
    return HttpResponse("<h3>hola segunda vista  </h3>")

