from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.views.generic import DetailView , UpdateView, DeleteView
from django.http import JsonResponse


def booking(request):
    error = ''

    if request.method == 'POST':
        form = BookingForm(request.POST)
        #create valid form for date
        #create sum function
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            form.save()
            return redirect('account')
        else:
            error = 'Форма не корректна'

    form = BookingForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'bookings/booking.html', context)

# class bookinginformations(DeleteView):
#     model = Booking
#     success_url = 'account'
#     template_name = 'bookings/bookinginformations.html'

def get_date(request):
    firstdate = request.POST.get("startdate", "")
    lastdate = request.POST.get("finishdate", "")

    response = {}

    try:
        response['result'] = 'True'
        response['message'] = firstdate
    except:
        response['result'] = 'False'
        response['message'] = 'error'
    return HTTPResponse(json.dumps(response), context_type="applications/json" )


class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'main/booking_update.html'
    success_url = '/account'

class BookingDeleteView(DeleteView):
    model = Booking
    success_url = '/account'
    template_name = 'main/booking_delete.html'
