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
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'create_form.html', context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'listing_update.html', context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')