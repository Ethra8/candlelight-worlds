from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the most recent information on the site.
    Displays an individual instance of :model:`about.About`.

    """
    about = About.objects.all().order_by('-updated_on').first()

    template = "about/about.html"
    context = {
            "about": about,
        }

    return render(request, template, context)