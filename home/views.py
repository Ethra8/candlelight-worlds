from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


