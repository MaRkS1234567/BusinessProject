from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.db.models import Avg

from bookings.models import Booking
from .forms import AccountCreationForm, SigninForm, ReviewForm
from .models import Review


def index(request):
    return render(request, 'main/index.html')


def about(request):
    reviews = Review.objects.order_by('-id')
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    average = round(Review.objects.aggregate(Avg('stars'))['stars__avg'])

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('about')
        else:
            return render(request, 'main/about.html', {'form': form, 'page': page, 'average': average})

    form = ReviewForm()
    context = {
        'form': form,
        'page': page,
        'average': average
    }

    return render(request, 'main/about.html', context)


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
