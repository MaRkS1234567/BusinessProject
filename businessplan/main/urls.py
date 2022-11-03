from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.signin, name='login'),
    path('account', views.account, name='account'),
    path('logout', views.signout, name='logout'),
]
