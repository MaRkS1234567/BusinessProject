from dataclasses import field
from tkinter import Widget
from .models import Booking
from django.forms import ModelForm, DateTimeInput, TextInput


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['startdate', 'finishdate','pnumber', 'fullname']
        widgets = {
            "pnumber": TextInput(attrs={
                'class': 'form-control',
            }),
            "fullname": TextInput(attrs={
                'class': 'form-control',
            }),
            "startdate": DateTimeInput(attrs={
                'type' : 'date',
                'class': 'form-control',
            }),
            "finishdate": DateTimeInput(attrs={
                'type' : 'date',
                'class': 'form-control',
            }),
        }

