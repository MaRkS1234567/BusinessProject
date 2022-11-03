from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.conf import settings


class Booking(models.Model):
    startdate = models.DateField('Startgdate')
    finishdate = models.DateField('Finishdate')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField('Full name', max_length=50)
    pnumber = models.PositiveBigIntegerField('Phone number')
    # created_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        # ordering = ['-created_at']