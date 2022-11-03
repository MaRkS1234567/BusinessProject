from django.urls import path

from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('get_date', views.get_date, name='get_date'),
    path('update/<int:pk>', views.BookingUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.BookingDeleteView.as_view(), name='delete'),
]