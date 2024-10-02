from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import date

from .models import Booking



class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Book Now'))

    class Meta:
        model = Booking
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Add validation for 'date' field
    def clean_date(self):
        booking_date = self.cleaned_data.get('date')

        # Get today's date
        today = date.today()

        # Check if booking date is in past or today
        if booking_date <= today:
            raise ValidationError("You cannot book for today or past dates. Please select a future date.")

        return booking_date