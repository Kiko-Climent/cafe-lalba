from django import forms
from django.forms.widgets import DateInput
from .models import Booking
from datetime import time, date

"""Create New Booking Form"""
class BookingForm(forms.ModelForm):
    num_people = forms.IntegerField(
        label='Number of People',
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 5)]),
        min_value=1,
        max_value=4,
        required=True
    )

    start_time = forms.TimeField(
        widget=forms.Select(choices=[
            (time(hour=18), '18:00'),
            (time(hour=19), '19:00'),
            (time(hour=20), '20:00'),
            (time(hour=21), '21:00'),
        ]),
        required=True
    )

    date = forms.DateField(
        widget=forms.SelectDateWidget(),
        initial=date.today(),
        required=True
    )

    class Meta:
        model = Booking
        fields = ['name', 'num_people', 'start_time', 'date', 'phone', 'email', 'notes']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        date = cleaned_data.get('date')

        if date < date.today():
            raise forms.ValidationError("Cannot select a date in the past.")
        
        if date == date.today():
            raise forms.ValidationError("Reservations for today are not allowed.")
            
        if start_time and date:
            conflicting_bookings = Booking.objects.filter(
                start_time=start_time,
                date=date
            )
            if conflicting_bookings.count() >= 6:
                raise forms.ValidationError("Exceeded maximum bookings for this hour.")
        
        return cleaned_data
    

""" Form to update an existing booking"""
class BookingUpdateForm(forms.ModelForm):
    num_people = forms.IntegerField(
        label='Number of People',
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 5)]),
        min_value=1,
        max_value=4,
        required=True
    )

    start_time = forms.TimeField(
        widget=forms.Select(choices=[
            (time(hour=18), '18:00'),
            (time(hour=19), '19:00'),
            (time(hour=20), '20:00'),
            (time(hour=21), '21:00'),
        ]),
        required=True
    )

    date = forms.DateField(
        widget=forms.SelectDateWidget(),
        initial=date.today(),
        required=True
    )

    class Meta:
        model = Booking
        fields = ['start_time', 'date', 'num_people']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        date = cleaned_data.get('date')

        if date < date.today():
            raise forms.ValidationError("Cannot select a date in the past.")
            
        if start_time and date:
            conflicting_bookings = Booking.objects.filter(
                start_time=start_time,
                date=date
            )
            if conflicting_bookings.exclude(id=self.instance.id).count() >= 6:
                raise forms.ValidationError("Exceeded maximum bookings for this hour.")
        
        return cleaned_data

    """make update booking not be able to reserve a table in the past"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = DateInput(attrs={'type': 'date', 'min': str(date.today())})
       