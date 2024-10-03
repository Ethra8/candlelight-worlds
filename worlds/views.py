from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import World


# Create your views here.
class WorldList(generic.ListView):
    queryset = World.objects.all()
    template_name = "worlds/worlds.html"


def world_details(request, pk):
    """
    Display an individual model:`worlds.World`. on
    worlds/world_details.html page
    """
    queryset = World.objects.all()
    world = get_object_or_404(queryset, pk=pk)

    template = 'worlds/world_details.html'
    context = {
        "world": world,
    }

    return render(request, template, context)
