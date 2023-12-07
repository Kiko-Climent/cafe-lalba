from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
# To check availability
from datetime import timedelta

@login_required

def new_reservation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user if request.user.is_authenticated else None

            # Check reservation limits for the day
            reservations_today = Booking.objects.filter(date=booking.date)
            if reservations_today.count() >= 6:  # Adjust to your maximum daily limit
                messages.error(request, 'Daily reservations limit reached.')
                return redirect('reservation_page')  # Change 'reservation_page' to your actual URL name

            # Check table availability for the requested time
            start_time = booking.date  # Adjust with actual start time from the form
            end_time = start_time + timedelta(hours=2)  # Assuming 2 hours per booking
            colliding_reservations = Booking.objects.filter(date=booking.date).exclude(
                id=booking.id if booking.id else None
            ).filter(date__range=(start_time, end_time))
            if colliding_reservations.exists():
                messages.error(request, 'Table already booked for the requested time.')
                return redirect('reservation_page')  # Change 'reservation_page' to your actual URL name

            booking.save()

            # Generate a booking report
            reservation_details = {
                'name': booking.name,
                'num_people': booking.num_people,
                'date': booking.date,
                'phone': booking.phone,
                'email': booking.email,
                'notes': booking.notes,
            }
            report_html = render_to_string('reservations/reservation_report.html', {
                'reservation_details': reservation_details
            })
            # Display a success message to the user
            messages.success(request, 'Reservation successfully made')
            # Return an HTTP response with the report
            return HttpResponse(report_html)
        else:
            messages.error(request, 'Something went wrong, please check your data')
    else:
        form = BookingForm()

    return render(request, 'reservations/new_reservation.html', {'form': form})

@login_required

def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

