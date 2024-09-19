from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import World


# Create your views here.
class WorldList(generic.ListView):
    queryset = World.objects.all()
    template_name = "worlds/worlds.html"


def world_details(request, slug):
    """
    Display an individual model:`worlds.World`. on 
    worlds/worlds.html page
    """
    queryset = World.objects.all()
    world = get_object_or_404(queryset, slug=slug)
    
    price = world.price
    description = world.description

    template = 'worlds/world_details.html'
    context = {
        "world": world,
        "slug": slug,
        "price": price,
        "description": description,
    }

    return render(request, template, context)

    # queryset = World.objects.all()
    # world = get_object_or_404(queryset, slug=slug)
    # price = get_object_or_404(queryset, price=price)
    # # short_description = get_object_or_404(queryset, short_description=world.short_description)
    # description = get_object_or_404(queryset, description=world.description)

    # template = 'worlds/world_details.html'
    # context = {
    #         "world": world,
    #         "slug": slug,
    #         "price": price,
    #         # 'short_description': short_description,
    #         "description": description,
    #     }

    # return render(request, template, context)
