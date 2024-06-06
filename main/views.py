from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def home(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    profiles = Profile.objects.all()
    return render(request, 'main/home.html', {'form': form, 'profiles': profiles})
