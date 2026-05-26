from django.shortcuts import render
from .models import Highlight

# Create your views here.

def home(request):
    # Fetch all the highlights that are saved in my database
    highlights = Highlight.objects.all() 
    
    # Send them to my HTML page as a variable called "highlights"
    return render(request, 'marketplace/home.html', {'highlights': highlights})