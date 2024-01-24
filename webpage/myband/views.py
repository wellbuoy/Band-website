from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event

def home(request):
    return render(request, 'band/home.html')

def about(request):
    return render(request, 'band/about.html')

@login_required
def events(request):
    events = Event.objects.all()
    return render(request, 'band/events.html', {'events': events})
