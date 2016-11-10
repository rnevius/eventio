from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone

from .forms import AddEventForm
from .models import Event

def index(request):
    events = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'index.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})


@login_required
def event_add(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('event', pk=event.pk)
    else:
        form = AddEventForm()
    return render(request, 'event_add.html', {'form': form})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.user != event.owner:
        raise PermissionDenied

    event.delete()
    messages.success(request, 'Event Deleted')
    return redirect('/')


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
