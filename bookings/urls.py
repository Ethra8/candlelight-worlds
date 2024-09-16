from django.urls import path
from .views import CreateBookingView, BookingListView, BookingUpdateView, BookingDeleteView
from . import views


urlpatterns = [
    path('new/', views.CreateBookingView.as_view(), name='booking_new'),
    path('update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),
    path('manage/', BookingListView.as_view(), name='booking_list'),
    path('delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_confirm_delete'),
]