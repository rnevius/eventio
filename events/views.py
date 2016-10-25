from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

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


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.user != event.owner:
        raise PermissionDenied

    if request.method == 'POST':
        form = AddEventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event', pk=event.pk)
    else:
        form = AddEventForm(instance=event)

    return render(request, 'event_edit.html', {'form': form})


@login_required
def event_register(request, pk):
    event = get_object_or_404(Event, pk=pk)
    request.user.attending_events.add(event)

    return render(request, 'event_register.html', {'event': event})
