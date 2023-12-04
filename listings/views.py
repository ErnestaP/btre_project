from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from listings.choices import price_choices, bedroom_choices, state_choice

def index(request): #main listings page
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # objects.all() will fetch all the listings, order_by('-list_date') descending order (the most recent on top), for filter we are passing the name of our filed, and how we want to filter
    paginator = Paginator(listings, 6) # 6 per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id) # if we will go to the listing that we don't have, it will show 404, listing id is passed by url
    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) #description__icontains; __icontains gives full text search in description
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) #city__iexact; __iexact gives exact match in cities (i gives case insensitive, exact - case sensitive)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) #city__iexact; __iexact gives exact match in cities (i gives case insensitive, exact - case sensitive)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) #lte less or equal

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) #lte less or equal


    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choice': state_choice,
        'listings': queryset_list,
        'values': request.GET, # passing all the args from request,
    }
    return render(request, 'listings/search.html', context)