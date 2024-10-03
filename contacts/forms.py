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
        fields = ['name', 'company_name', 'email', 'message']

    # Customizing the 'message' field's widget
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,  # Limit the number of rows to 4
                'placeholder': 'Enter your message here...',  # noqa Optional: Add placeholder text
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Prepopulate the email field if the user is authenticated
        if user and user.is_authenticated:
            self.fields['email'].initial = user.email

            print(user.username)
