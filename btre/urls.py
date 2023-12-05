"""
URL configuration for btre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# paths are linked to a view method
# or we can link to url from another file like here we are linking to admin urls
# when we are creating listing app, it will create new folder called listings
# and we want to create new urls.py in that listings app
# and in the main urls.py we will bring that in as its done with admin
# any specific route that we want like: listings/add, we will put in listings/url.py
# global is url.py is like collection of all of the urls

urlpatterns = [
    path('', include('pages.urls')), # empty, because we just want to have it in home page
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
