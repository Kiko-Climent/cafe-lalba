from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages

@login_required

def new_reservation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user if request.user.is_authenticated else None
            booking.save()

        else:
            messages.error(request, 'Something went wrong, please check your data')
    else:
        form = BookingForm()

    return render(request, 'reservations/new_reservation.html', {'form': form})

@login_required

def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

