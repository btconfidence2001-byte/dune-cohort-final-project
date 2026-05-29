from django.shortcuts import render
from .models import Listing, Highlight


def home_view(request):
    active_listings = Listing.objects.filter(
        status=Listing.Status.ACTIVE, 
        is_available=True
    )
    
    try:
        all_highlights = Highlight.objects.all()
    except Exception:
        all_highlights = []

    context = {
        'listings': active_listings,
        'highlights': all_highlights
    }
    
    return render(request, 'marketplace/home.html', context)