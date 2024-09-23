from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactRequest
from .forms import ContactForm


def contact_form(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, user=request.user)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user if request.user.is_authenticated else None
            contact.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your request has been successfully received.<br> We endeavour to respond within 2 working days.'  # noqa
            )
            return redirect('index')
    else:
        contact_form = ContactForm(user=request.user)

    return render(request, 'contacts/contact.html', {'contact_form': contact_form})