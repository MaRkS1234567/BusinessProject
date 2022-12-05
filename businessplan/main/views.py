from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, get_user_model
from django.views.generic import UpdateView

from bookings.models import Booking
from .forms import AccountCreationForm, SigninForm



def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Вы успешно вошли в аккакнт,{form.data["username"]}!')
            return redirect('login')
        return render(request, 'main/register.html', {'form': form})
    form = AccountCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'main/register.html', context)


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(
                request, f'Вы успешно вошли в свой аккаунт, {form.data["username"]} !')
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'form': form})

    form = SigninForm()
    context = {'form': form}

    return render(request, 'main/login.html', context)

def signout(request):
    logout(request)
    return redirect('home')


def account(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-id')

    for booking in bookings:
        price = 3700 * (booking.finishdate - booking.startdate).days
        booking.price = price

    context = {
        'bookings': bookings
    }
    return render(request, 'main/account.html', context)
