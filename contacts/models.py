from django.db import models
from django.contrib.auth.models import User


class ContactRequest(models.Model):
    """
    Stores a contact request message
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Reference to User
    name = models.CharField(max_length=200, null=False, blank=False)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=80, null=False, blank=False)
    message = models.TextField(max_length=80, null=False, blank=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact form sent by {self.name}"


