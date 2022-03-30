from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Flat
from .forms import FlatForm
from .forms import RegisterForm, LoginForm


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


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form': form})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            print(form.errors)
        return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()
        return render(request, "form.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")