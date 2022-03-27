from django.shortcuts import render, redirect
from .models import Flat
from .forms import FlatForm

def index(request):
    flats = Flat.objects.all()
    return render(request, 'main/index.html', {'title':'Главная', 'flats': flats})

def about(request):
    return render(request, 'main/about.html')

def hellp(request):
    return render(request, 'main/hellp.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = FlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма не коректна"

    form = FlatForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)