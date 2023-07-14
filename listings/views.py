from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
# Create your views here.

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': listings})

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    return render(request, 'listing.html', {'listing': listing}) 

def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'create_form.html', context)