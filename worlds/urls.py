from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from .views import WorldList, world_details


urlpatterns = [
    path('', views.WorldList.as_view(), name='worlds'),
    path('world_details/<int:pk>/', views.world_details, name='world_details'),
]