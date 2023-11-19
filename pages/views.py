from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html') # (request, template)

def about(request):
    return render(request, 'pages/about.html') # (request, template)