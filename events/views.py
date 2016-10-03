from django.shortcuts import render, get_object_or_404

from .models import Event

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})
