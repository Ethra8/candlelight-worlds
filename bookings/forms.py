from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
        }