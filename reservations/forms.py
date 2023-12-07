from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    num_people = forms.IntegerField(
        label='Number of People',
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 9)]),  
        min_value=1,
        max_value=8,
    )

    class Meta:
        model = Booking
        fields = ['name', 'num_people', 'date','start_time', 'end_time', 'phone', 'email', 'notes']
        input_formats = {
            'date': ['%d/%m/%Y']
        }
