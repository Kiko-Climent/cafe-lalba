from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from .forms import BookingUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta

@login_required

def new_reservation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user if request.user.is_authenticated else None
            
            if booking.date and booking.start_time and booking.end_time:
                start_time = booking.start_time
                end_time = booking.end_time
                # Obtener reservas para la misma fecha y hora
                colliding_reservations = Booking.objects.filter(date=booking.date).exclude(
                    id=booking.id if booking.id else None
                ).filter(start_time__lte=end_time, end_time__gte=start_time)
                
                if colliding_reservations.count() >= 6:
                    # Verificar si ya han pasado 2 horas desde la última reserva
                    last_booking_time = colliding_reservations.latest('date_added').date_added
                    if last_booking_time + timedelta(hours=2) > timezone.now():
                        messages.error(request, 'Fully booked for this hour. Try another time.')
                        return render(request, 'reservations/new_reservation.html', {'form': form})

            booking.save()


            # Generate a booking report
            reservation_details = {
                'name': booking.name,
                'num_people': booking.num_people,
                'start_time': booking.start_time,
                'end_time': booking.end_time,
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
def user_reservation(request):
    user_bookings = Booking.objects.filter(user=request.user)
    if user_bookings.exists():
        active_booking = user_bookings.first()
        if active_booking.user == request.user:
            print("User and active booking associated correctly:", request.user, active_booking.id)
            return render(request, 'reservations/update_reservation.html', {'form': BookingForm(instance=active_booking), 'booking': active_booking})
    return redirect('new_reservation')



@login_required

def reservation_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html', {'bookings': bookings})


@login_required
def update_reservation(request, booking_id):
    print("Received booking ID:", booking_id)
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingUpdateForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully')
            return redirect('reservation_list')
    else:
        form = BookingUpdateForm(instance=booking)

    return render(request, 'reservations/update_reservation.html', {'form': form, 'booking': booking})
    
"""Add view to cancel an existing reservation"""
@login_required
def delete_reservation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Reservation deleted successfully')
        return redirect('reservation_list')

    return render(request, 'reservations/delete_reservation.html', {'booking': booking})

