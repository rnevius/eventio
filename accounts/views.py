from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save()
            # Log in the user
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
