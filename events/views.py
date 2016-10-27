from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddEventForm
from .models import Event

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})


def event_add(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event', pk=event.pk)
    else:
        form = AddEventForm()
    return render(request, 'event_add.html', {'form': form})
