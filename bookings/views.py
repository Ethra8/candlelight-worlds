from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Booking
from .forms import BookingForm


class CreateBookingView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        temp_booking = form.save(commit=False)
        # check if time/ date is available
        existing_bookings = Booking.objects\
            .filter(date=temp_booking.date)\
            .filter(time=temp_booking.time)\
            .filter(world=temp_booking.world)
            
        if existing_bookings :
            messages.warning(self.request, f'At {temp_booking.time} on {temp_booking.date}, our {temp_booking.world} is already booked')
            return redirect(reverse('booking_new'))
        else:
            messages.success(self.request, 'Your booking is confirmed')
            temp_booking.save()
        return redirect(reverse('booking_list'))


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs).order_by('date')
       return qs.filter(user=self.request.user)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm  # Use BookingForm instead of fields
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        # Make sure that booking can only be accessed by the logged-in user
        if form.instance.user != self.request.user:
            messages.warning(self.request, 'You can only update your own bookings!')
            return redirect(reverse('booking_list'))

        temp_booking = form.save(commit=False)
        # Check if the time/date is available
        existing_bookings = Booking.objects\
            .filter(date=temp_booking.date)\
            .filter(world=temp_booking.world)

        if existing_bookings:
            messages.warning(self.request, f'At {temp_booking.time} on {temp_booking.date}, our {temp_booking.world} is already booked')
            return redirect(f'/bookings/update/{temp_booking.pk}/')
        else:
            messages.success(self.request, "Your booking's changes are confirmed!")
            temp_booking.save()

        return redirect(f'/bookings/manage/')


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')
    
    # add def post() instead of delete() to avoid booking getting deleted before showing message
    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Your booking has successfully been deleted.")
        return super().post(request, *args, **kwargs)