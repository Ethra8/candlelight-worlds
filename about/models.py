from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message
    """
    name = models.CharField(max_length=200, null=False, blank=False)
    company_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    message = models.TextField(max_length=80, null=False, blank=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"