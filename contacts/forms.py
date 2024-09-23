from django import forms
from .models import ContactRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from .models import ContactRequest

from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'company_name', 'email', 'message']  # No 'user' field

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Prepopulate the name and email fields if the user is authenticated
        if user and user.is_authenticated:
            self.fields['name'].initial = user.get_full_name() or user.username
            self.fields['email'].initial = user.email

