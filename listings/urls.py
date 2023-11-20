from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="listings"), # (means /listings page, method, name to easily access this path)
    path('<int:listing_id>', views.listing, name="listing"), # (will be like listings/34, method name, name of url_
    path('search', views.search, name="search"), #
]