from django.shortcuts import render
from .models import Listing
# Create your views here.

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': listings})

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    return render(request, 'listing.html', {'listing': listing})    