from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import World


# Create your views here.
class WorldList(generic.ListView):
    queryset = World.objects.all()
    template_name = "worlds/worlds.html"


def world_details(request, slug):
    """
    Display an individual :model:`worlds.World`.
    **Context**
    ``world``
        An instance of :model:`worlds.World`.
    
    **Template:**
    :template:`worlds/world_details.html`
    """
    queryset = World.objects.all()
    world = get_object_or_404(queryset, slug=slug)
    description = get_object_or_404(queryset, description=world.description)

    return render(
        request,
        "worlds/world_details.html",
        {
            "world": world,
            "slug": slug,
            "description": description,
        },
    )
