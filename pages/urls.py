from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # (means home page, method, name to easily access this path)
    path('about', views.about, name="about"),
]