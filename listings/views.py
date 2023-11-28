from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

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
    return render(request, 'listings/search.html')